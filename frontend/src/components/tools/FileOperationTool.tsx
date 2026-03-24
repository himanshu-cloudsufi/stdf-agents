import { memo, useMemo } from "react";
import { FileSearch, FilePlus, FileEdit } from "lucide-react";
import type { ToolComponentProps } from "./ToolCard";
import { ToolCard } from "./ToolCard";
import { safeParseJson } from "../../utils/safeParseJson";

type FileVariant = "Read" | "Write" | "Edit";

interface FileOperationInput {
  file_path?: string;
  old_string?: string;
  new_string?: string;
  content?: string;
  offset?: number;
  limit?: number;
}

interface FileOperationProps extends ToolComponentProps {
  variant: FileVariant;
}

const variantConfig: Record<
  FileVariant,
  { icon: React.ReactNode; verb: string; verbPast: string }
> = {
  Read: {
    icon: <FileSearch className="h-3.5 w-3.5" />,
    verb: "Reading",
    verbPast: "Read",
  },
  Write: {
    icon: <FilePlus className="h-3.5 w-3.5" />,
    verb: "Creating file",
    verbPast: "Created",
  },
  Edit: {
    icon: <FileEdit className="h-3.5 w-3.5" />,
    verb: "Editing",
    verbPast: "Edited",
  },
};

function shortPath(filePath: string): string {
  const parts = filePath.split("/");
  return parts.length > 2 ? parts.slice(-2).join("/") : filePath;
}

function truncate(s: string, max: number): string {
  if (s.length <= max) return s;
  return s.slice(0, max) + "...";
}

const FileOperationToolInner: React.FC<FileOperationProps> = ({
  block,
  variant,
}) => {
  const config = variantConfig[variant];
  const input = useMemo(
    () => safeParseJson<FileOperationInput>(block.input, {}),
    [block.input],
  );

  const filePath = input.file_path ?? "";
  const displayPath = filePath ? shortPath(filePath) : "file";

  const hasEditDetail =
    variant === "Edit" && Boolean(input.old_string || input.new_string);

  return (
    <ToolCard
      icon={config.icon}
      status={block.status}
      title={(status) => {
        if (status === "done") {
          if (variant === "Write") return `${config.verbPast} ${displayPath}`;
          return `${config.verbPast} ${displayPath}`;
        }
        if (variant === "Write") return `Creating file ${displayPath}`;
        return `${config.verb} ${displayPath}`;
      }}
      expandable={hasEditDetail}
    >
      {hasEditDetail && (
        <div className="space-y-1 text-[11px] font-mono text-gray-500">
          {input.old_string && (
            <div>
              <span className="text-red-500 select-none">- </span>
              <span className="text-red-600">
                {truncate(input.old_string, 120)}
              </span>
            </div>
          )}
          {input.new_string && (
            <div>
              <span className="text-green-500 select-none">+ </span>
              <span className="text-green-600">
                {truncate(input.new_string, 120)}
              </span>
            </div>
          )}
        </div>
      )}
    </ToolCard>
  );
};

const FileOperationToolMemo = memo(FileOperationToolInner);

/** Pre-bound variants for the registry */
export const ReadTool: React.FC<ToolComponentProps> = (props) => (
  <FileOperationToolMemo {...props} variant="Read" />
);
export const WriteTool: React.FC<ToolComponentProps> = (props) => (
  <FileOperationToolMemo {...props} variant="Write" />
);
export const EditTool: React.FC<ToolComponentProps> = (props) => (
  <FileOperationToolMemo {...props} variant="Edit" />
);
