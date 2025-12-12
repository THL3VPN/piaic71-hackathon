---
id: 0009
title: next-setup-and-env
stage: tasks
date: 2025-12-12
surface: specs
model: gpt-5
feature: 001-spec-meta
branch: 001-spec-meta
user: aie
command: manual (scaffold Next.js with Better Auth placeholders)
labels: [tasks, frontend, env, tests]
links:
  spec: specs/001-spec-meta/spec.md
  plan: specs/001-spec-meta/plan.md
  tasks: specs/001-spec-meta/tasks.md
files:
  - path: frontend/package.json
    note: Added Next.js App Router + Better Auth deps and scripts.
  - path: frontend/tsconfig.json
    note: TS config for Next.js.
  - path: frontend/next.config.js
    note: Next.js config.
  - path: frontend/tailwind.config.js
    note: Tailwind setup.
  - path: frontend/postcss.config.js
    note: PostCSS config.
  - path: frontend/next-env.d.ts
    note: Next.js TS env hints.
  - path: frontend/app/layout.tsx
    note: Root layout using globals.css.
  - path: frontend/app/globals.css
    note: Tailwind base import.
  - path: frontend/lib/auth.ts
    note: Better Auth placeholders for sign-in/up/session.
  - path: frontend/lib/api.ts
    note: API client attaching JWT/user_id.
  - path: frontend/components/TaskForm.tsx
  - path: frontend/components/TaskItem.tsx
  - path: frontend/components/TaskList.tsx
  - path: frontend/app/login/page.tsx
  - path: frontend/app/signup/page.tsx
  - path: frontend/app/tasks/page.tsx
    note: Task dashboard wired to API client with session placeholder.
  - path: specs/001-spec-meta/tasks.md
    note: Updated completion status for frontend/env tasks.
  - path: specs/001-spec-meta/research.md
    note: Added env handling decision.
  - path: specs/001-spec-meta/quickstart.md
    note: Added env vars and sample .env example reference.
  - path: specs/001-spec-meta/spec.md
    note: Added rule priority/edit policy summary.
  - path: specs/001-spec-meta/plan.md
    note: Added validation note.
tests:
  - status: pass
    note: UV_CACHE_DIR=.uv-cache uv run pytest (79 passed, 100% coverage)
---

## Prompt

do the remaining work

## Response snapshot

Scaffolded a Next.js App Router structure with Tailwind and Better Auth placeholders (package.json, configs, layout, globals, auth/api clients, auth pages, task dashboard, task components). Added .env.example, env notes in quickstart/research, rule/edit summary in spec, validation note in plan. Updated tasks.md to mark frontend/env polish complete. Reran `UV_CACHE_DIR=.uv-cache uv run pytest` (79 passed, 100% coverage).

## Outcome

- ✅ Next.js frontend scaffolded with placeholder Better Auth hooks and task UI.
- ✅ Env docs and sample .env in repo.
- ✅ Specs/plan updated for rule summary and validation note.
- ✅ Tasks file updated to reflect completion.
- ✅ Tests pass (backend CLI suite unaffected).
- 🔁 Next: replace Better Auth placeholders with real integration and run frontend build/lint when ready.
- 🧠 Reflection: Keep using local uv cache for pytest; frontend still needs actual Better Auth wiring.

## Evaluation notes (flywheel)

- Failure modes observed: none; tests unaffected.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): Integrate Better Auth for real session/JWT issuance and attach to API client.
