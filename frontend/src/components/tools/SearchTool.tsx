import { memo, useMemo } from "react";
import { Search, FolderSearch } from "lucide-react";
import type { ToolComponentProps } from "./ToolCard";
import { ToolCard } from "./ToolCard";
import { safeParseJson } from "../../utils/safeParseJson";

type SearchVariant = "Grep" | "Glob";

interface SearchInput {
  pattern?: string;
  path?: string;
  glob?: string;
  type?: string;
  output_mode?: string;
}

interface SearchProps extends ToolComponentProps {
  variant: SearchVariant;
}

const variantConfig: Record<
  SearchVariant,
  { icon: React.ReactNode; label: string }
> = {
  Grep: {
    icon: <Search className="h-3.5 w-3.5" />,
    label: "Search",
  },
  Glob: {
    icon: <FolderSearch className="h-3.5 w-3.5" />,
    label: "Find files",
  },
};

function shortPath(p: string): string {
  const parts = p.split("/");
  return parts.length > 2 ? parts.slice(-2).join("/") : p;
}

const SearchToolInner: React.FC<SearchProps> = ({ block, variant }) => {
  const config = variantConfig[variant];
  const input = useMemo(
    () => safeParseJson<SearchInput>(block.input, {}),
    [block.input],
  );

  const pattern = input.pattern ?? "";
  const hasDetails = Boolean(input.path) || Boolean(input.glob) || Boolean(input.type);

  return (
    <ToolCard
      icon={config.icon}
      status={block.status}
      title={pattern ? `${config.label}: ${pattern}` : `${config.label}...`}
      expandable={hasDetails}
      statusDetail={
        hasDetails ? (
          <span className="text-[10px] text-gray-400">
            {input.path ? shortPath(input.path) : ""}
            {input.glob ? ` glob:${input.glob}` : ""}
            {input.type ? ` type:${input.type}` : ""}
          </span>
        ) : undefined
      }
    >
      {hasDetails && (
        <div className="text-[11px] text-gray-500 space-y-0.5">
          {input.path && (
            <div>
              <span className="text-gray-400">Path: </span>
              {shortPath(input.path)}
            </div>
          )}
          {input.glob && (
            <div>
              <span className="text-gray-400">Filter: </span>
              {input.glob}
            </div>
          )}
          {input.type && (
            <div>
              <span className="text-gray-400">Type: </span>
              {input.type}
            </div>
          )}
          {input.output_mode && (
            <div>
              <span className="text-gray-400">Mode: </span>
              {input.output_mode}
            </div>
          )}
        </div>
      )}
    </ToolCard>
  );
};

const SearchToolMemo = memo(SearchToolInner);

/** Pre-bound variants for the registry */
export const GrepTool: React.FC<ToolComponentProps> = (props) => (
  <SearchToolMemo {...props} variant="Grep" />
);
export const GlobTool: React.FC<ToolComponentProps> = (props) => (
  <SearchToolMemo {...props} variant="Glob" />
);
