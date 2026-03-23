const wsProto = window.location.protocol === "https:" ? "wss:" : "ws:";
const wsPort = window.location.port ? `:${window.location.port}` : "";
export const WS_URL = `${wsProto}//${window.location.hostname}${wsPort}/ws`;
export const DEFAULT_USER_ID = "user";
