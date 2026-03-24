import { memo, useMemo } from "react";
import { Terminal } from "lucide-react";
import type { ToolComponentProps } from "./ToolCard";
import { ToolCard } from "./ToolCard";
import { safeParseJson } from "../../utils/safeParseJson";

interface BashInput {
  command?: string;
  description?: string;
  timeout?: number;
  run_in_background?: boolean;
}

const BashToolInner: React.FC<ToolComponentProps> = ({ block }) => {
  const input = useMemo(
    () => safeParseJson<BashInput>(block.input, {}),
    [block.input],
  );

  const command = input.command ?? "";
  const description = input.description;

  const title = useMemo(() => {
    if (description) return description;
    if (command) {
      return command.length > 80 ? command.slice(0, 80) + "..." : command;
    }
    return "Running command...";
  }, [description, command]);

  const hasExpandableContent = command.length > 60;

  return (
    <ToolCard
      icon={<Terminal className="h-3.5 w-3.5" />}
      status={block.status}
      title={(status) => {
        switch (status) {
          case "done":
            return title;
          case "running":
            return description ? description : command ? `Running: ${command.slice(0, 60)}` : "Running command...";
          default:
            return title;
        }
      }}
      expandable={hasExpandableContent}
    >
      {hasExpandableContent && (
        <pre className="whitespace-pre-wrap break-all font-mono text-[11px] leading-relaxed text-gray-500">
          <span className="select-none text-gray-400">$ </span>
          {command}
        </pre>
      )}
    </ToolCard>
  );
};

export const BashTool = memo(BashToolInner);
