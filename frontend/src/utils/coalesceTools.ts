import type { ContentBlock, ToolCallBlock } from "../types";

/**
 * Coalesce consecutive completed Read tool-call blocks into a single
 * synthetic "ReadCoalesced" block so the UI can render "Read N files"
 * instead of N separate cards.
 *
 * Rules:
 *  - Only consecutive `tool_call` blocks with `name === "Read"` AND
 *    `status === "done"` are eligible for coalescing.
 *  - A single Read block passes through unchanged.
 *  - The synthetic block uses `name: "ReadCoalesced"` and its `input`
 *    is a JSON array of the original file paths.
 */
export function coalesceBlocks(blocks: ContentBlock[]): ContentBlock[] {
  const result: ContentBlock[] = [];
  let readRun: ToolCallBlock[] = [];

  function flushRun() {
    if (readRun.length <= 1) {
      // Single or zero — pass through as-is
      for (const b of readRun) {
        result.push(b);
      }
    } else {
      // Extract file paths from each Read block's input
      const filePaths: string[] = readRun.map((b) => {
        try {
          const parsed = JSON.parse(b.input) as { file_path?: string };
          return parsed.file_path ?? "unknown";
        } catch {
          return "unknown";
        }
      });

      const synthetic: ToolCallBlock = {
        type: "tool_call",
        toolId: `coalesced-${readRun[0].toolId}`,
        name: "ReadCoalesced",
        input: JSON.stringify(filePaths),
        status: "done",
        subEvents: [],
      };
      result.push(synthetic);
    }
    readRun = [];
  }

  for (const block of blocks) {
    if (
      block.type === "tool_call" &&
      block.name === "Read" &&
      block.status === "done"
    ) {
      readRun.push(block);
    } else {
      flushRun();
      result.push(block);
    }
  }

  flushRun();
  return result;
}
