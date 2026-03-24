/**
 * Safely parse a JSON string, returning a fallback value on any error.
 *
 * During streaming, tool input arrives as an incrementally-built JSON string
 * that may be incomplete. This helper gracefully handles:
 *   - Valid JSON
 *   - Empty / blank strings
 *   - Partial / truncated JSON (mid-stream)
 *   - Any other malformed input
 */
export function safeParseJson<T>(input: string, fallback: T): T {
  if (!input || input.trim().length === 0) return fallback;
  try {
    return JSON.parse(input) as T;
  } catch {
    return fallback;
  }
}
