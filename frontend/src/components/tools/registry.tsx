/**
 * Tool Component Registry
 *
 * Maps tool names to lazily-loaded React components. Uses a singleton cache
 * so each component module is only imported once.
 */
import { lazy, type ComponentType } from "react";
import type { ToolComponentProps } from "./ToolCard";

type ToolComponent = ComponentType<ToolComponentProps>;
type ToolModuleLoader = () => Promise<{ default: ToolComponent }>;

// ---------------------------------------------------------------------------
// Module loaders — each maps a tool name to a lazy import
// ---------------------------------------------------------------------------
const toolLoaders: Record<string, ToolModuleLoader> = {
  Bash: () =>
    import("./BashTool").then((m) => ({ default: m.BashTool })),

  // File operations
  Read: () =>
    import("./FileOperationTool").then((m) => ({ default: m.ReadTool })),
  Write: () =>
    import("./FileOperationTool").then((m) => ({ default: m.WriteTool })),
  Edit: () =>
    import("./FileOperationTool").then((m) => ({ default: m.EditTool })),

  // Search tools
  Grep: () =>
    import("./SearchTool").then((m) => ({ default: m.GrepTool })),
  Glob: () =>
    import("./SearchTool").then((m) => ({ default: m.GlobTool })),

  // Web tools
  WebSearch: () =>
    import("./WebSearchTool").then((m) => ({ default: m.WebSearchVariant })),
  WebFetch: () =>
    import("./WebSearchTool").then((m) => ({ default: m.WebFetchVariant })),

  // Agent
  Agent: () =>
    import("./AgentTool").then((m) => ({ default: m.AgentTool })),

  // Coalesced reads (synthetic block from coalesceTools)
  ReadCoalesced: () =>
    import("./ReadCoalescedTool").then((m) => ({ default: m.ReadCoalescedTool })),
};

// Default fallback loader
const defaultLoader: ToolModuleLoader = () =>
  import("./DefaultTool").then((m) => ({ default: m.DefaultTool }));

// ---------------------------------------------------------------------------
// Singleton cache — ensures React.lazy returns the same component reference
// for repeated calls with the same tool name.
// ---------------------------------------------------------------------------
const cache = new Map<string, React.LazyExoticComponent<ToolComponent>>();

function getOrCreate(
  key: string,
  loader: ToolModuleLoader,
): React.LazyExoticComponent<ToolComponent> {
  const existing = cache.get(key);
  if (existing) return existing;
  const component = lazy(loader);
  cache.set(key, component);
  return component;
}

/**
 * Return the lazily-loaded component for the given tool name.
 * Unknown tools fall back to DefaultTool.
 */
export function getToolComponent(
  toolName: string,
): React.LazyExoticComponent<ToolComponent> {
  const loader = toolLoaders[toolName];
  if (loader) {
    return getOrCreate(toolName, loader);
  }
  return getOrCreate(toolName, defaultLoader);
}
