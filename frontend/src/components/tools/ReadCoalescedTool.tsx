import { memo, useMemo } from "react";
import { Files } from "lucide-react";
import type { ToolComponentProps } from "./ToolCard";
import { ToolCard } from "./ToolCard";
import { safeParseJson } from "../../utils/safeParseJson";

function shortPath(filePath: string): string {
  const parts = filePath.split("/");
  return parts.length > 2 ? parts.slice(-2).join("/") : filePath;
}

const ReadCoalescedToolInner: React.FC<ToolComponentProps> = ({ block }) => {
  const filePaths = useMemo(
    () => safeParseJson<string[]>(block.input, []),
    [block.input],
  );

  const count = filePaths.length;

  return (
    <ToolCard
      icon={<Files className="h-3.5 w-3.5" />}
      status={block.status}
      title={`Read ${count} file${count !== 1 ? "s" : ""}`}
      expandable={count > 0}
    >
      {count > 0 && (
        <div className="space-y-0.5 text-[11px] text-gray-500">
          {filePaths.map((fp, i) => (
            <div key={i} className="flex items-center gap-1">
              <span className="text-green-500 text-[10px] shrink-0">
                {"\u2713"}
              </span>
              <span className="truncate" title={fp}>
                {shortPath(fp)}
              </span>
            </div>
          ))}
        </div>
      )}
    </ToolCard>
  );
};

export const ReadCoalescedTool = memo(ReadCoalescedToolInner);
