---
name: show-report
description: Starts a local Python HTTP server and opens the STDF progress report in the browser. Triggers on 'show report', 'open report', 'view report', 'progress report', or '/show-report'.
---

# Show STDF Progress Report

Starts a local Python HTTP server serving the `reports/` directory and opens `stdf-progress-report.html` in the default browser.

## Usage

`/show-report`

No arguments needed.

## Execution

1. Pick an available port (default 8765).
2. Start `python3 -m http.server` serving the **repo root** (the report fetches `../output/` via relative paths).
3. Open the report in the default browser via `open` (macOS).
4. Report the URL to the user.
5. Tell the user to press Ctrl+C or run `kill <pid>` to stop the server when done.

Run:

```bash
PORT=8765
python3 -m http.server "$PORT" --directory /Users/himanshuchauhan/TONY/STDF/stdf-agents &
SERVER_PID=$!
sleep 0.5
open "http://localhost:${PORT}/reports/stdf-progress-report.html"
echo "Server running on http://localhost:${PORT} (PID: $SERVER_PID)"
echo "Stop with: kill $SERVER_PID"
```
