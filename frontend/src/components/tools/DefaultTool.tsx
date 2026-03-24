import { memo, useMemo } from "react";
import { Wrench } from "lucide-react";
import type { ToolComponentProps } from "./ToolCard";
import { ToolCard } from "./ToolCard";
import { getToolMetadata } from "../../utils/toolMetadata";

function tryPrettyPrint(raw: string): string {
  try {
    return JSON.stringify(JSON.parse(raw), null, 2);
  } catch {
    return raw;
  }
}

const DefaultToolInner: React.FC<ToolComponentProps> = ({ block }) => {
  const meta = useMemo(() => getToolMetadata(block.name), [block.name]);

  const hasInput = block.input.trim().length > 2;

  return (
    <ToolCard
      icon={<Wrench className="h-3.5 w-3.5" />}
      status={block.status}
      title={meta.description}
      expandable={hasInput}
    >
      {hasInput && (
        <pre className="whitespace-pre-wrap break-all font-mono text-[11px] leading-relaxed text-gray-500 max-h-48 overflow-y-auto">
          {tryPrettyPrint(block.input)}
        </pre>
      )}
    </ToolCard>
  );
};

export const DefaultTool = memo(DefaultToolInner);
