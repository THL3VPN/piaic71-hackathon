"use client";

import { useState } from "react";
import { signIn } from "../../lib/auth";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await signIn(email, password);
      // TODO: Redirect to /tasks after real Better Auth wiring
    } catch (err) {
      setError("Login failed");
      console.error(err);
    }
  };

  return (
    <main className="p-6 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Login</h1>
      <form onSubmit={handleSubmit} className="flex flex-col gap-3">
        <input
          className="border p-2"
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          className="border p-2"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button className="bg-blue-600 text-white px-4 py-2" type="submit">
          Sign In
        </button>
        {error && <p className="text-sm text-red-600">{error}</p>}
      </form>
      <p className="text-xs text-gray-600 mt-3">
        Better Auth integration placeholder. Wire to issue JWT and store securely.
      </p>
    </main>
  );
}
