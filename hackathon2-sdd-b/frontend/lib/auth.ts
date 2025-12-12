// Placeholder Better Auth integration helpers.
// Replace with real Better Auth client wiring (e.g., better-auth-next) when available.

export type Session = { token: string; userId: string };

export async function signIn(email: string, password: string): Promise<Session> {
  // TODO: Replace with Better Auth sign-in call
  return { token: "", userId: "" };
}

export async function signUp(email: string, password: string): Promise<Session> {
  // TODO: Replace with Better Auth signup call
  return { token: "", userId: "" };
}

export function getSession(): Session | null {
  // TODO: Read session/JWT from Better Auth store or cookies
  return null;
}

export function clearSession(): void {
  // TODO: Clear Better Auth session/JWT
}
