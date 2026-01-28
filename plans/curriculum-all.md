# Coding School Curriculum

## Course 0 — Developer Bearings: Terminal + VSCode + Git (no “real CS” yet)

Goal: feel comfortable navigating a codebase and running code before you learn concepts.

### Unit 0 — Terminal/CLI *(Language: Shell/CLI)*

- Terminal navigation: `pwd`, `ls`, `cd`
- Relative vs absolute paths
- More terminal commands: `touch`, `mkdir`, `cp`

### Unit 1 - VSCode essentials *(Language: VSCode + Shell/CLI)*
- Creating/editing files in VSCode (no fancy extensions yet—just open folder, edit, save)
- Running code from the VS terminal (the idea of “current directory” + “run this file”)
- Reading program output in the terminal (so “Printing” later makes sense)

### Unit 2 — Creating Python files *(Language: Python + Shell/CLI)*

- Creating `.py` files
- Running a Python file from the VSCode CLI vs running inside the editor

---

## Course 1 — Intro to Coding (Python)

Goal: go from “I can run a file” → “I can write small programs with control flow and functions.”

### Unit 1 — Output + basic programs *(Language: Python)*

- Printing
- Sequentiality (your code runs top-to-bottom; you can *store results in variables* and pass them to later steps)

### Unit 2 — Primitive types + strings *(Language: Python)*

- Primitive types (numbers, booleans, strings—just enough to proceed)
- String concat (build strings from pieces)

### Unit 3 — Functions (using and creating) *(Language: Python)*

- Using functions from a library (e.g., “lowercasing” a string)
- Creating your own functions (inputs → outputs)
- “Functions within functions” vs “assign then pass” (same idea, different readability tradeoffs)

### Unit 4 — Imports and libraries *(Language: Python)*

- Importing libraries (what an import *means* at a practical level)

### Unit 5 — Branching *(Language: Python)*

- If statements (how programs make decisions)

### Unit 6 — Loops: while *(Language: Python)*

- While loops (repeat until a condition changes)

### Unit 7 — Loops: for *(Language: Python)*

- For loops (repeat across a sequence of items)

### Unit 8 — Scope *(Language: Python)*

- Scope (what names are visible where; why “where you define something” matters)

### Unit 9 — Mutability vs immutability *(Language: Python)*

- Immutability vs mutability (when “changing something” mutates an object vs creates a new one)

---

## Course 2 — OOP + Core Language Fundamentals (Java)

Goal: become fluent in the “industry default” model of types, objects, and APIs—without drowning in theory.

### Unit 1 — Values vs references *(Language: Java)*

- Refs vs values (what actually gets copied when you assign/pass things)

### Unit 2 — OOP basics *(Language: Java)*

- OOP (objects as bundles of state + behavior)
- Classes (define the shape/behavior) vs instances (actual objects)

### Unit 3 — Abstraction tools *(Language: Java)*

- Interfaces (program to a capability, not an implementation)
- Inheritance (reuse + specialization—use carefully)
- Abstraction (hide complexity behind a clean surface)
- *(Footnote in this unit)* OOP is less “in style” in some modern codebases—still essential because huge systems and many interview/codebases assume it

### Unit 4 — Generic types *(Language: Java)*

- Generic types (write data structures and utilities that work over many types safely)

### Unit 5 — Concise expressions *(Language: Java)*

- Ternary (small conditional expression, not a replacement for clear logic)
- Lambdas (pass behavior as data—useful for callbacks, small transforms)

### Unit 6 — Copying + object identity *(Language: Java)*

- Deep vs shallow copying (copy the container vs copy the contained objects)
- How this interacts with refs vs values

### Unit 7 — Errors and defensive programming *(Language: Java)*

- Error handling, raising exceptions
- Defensive programming (validate inputs early; fail loudly with useful errors)

### Unit 8 — I/O and serialization *(Language: Java)*

- I/O (read/write data to files or streams)
- Serialization (turn in-memory objects into bytes/text and back)

### Unit 9 — Iteration models *(Language: Java)*

- Iterators (standard “walk a collection” interface)
- Iterators/generators (conceptual contrast: Java-style iteration vs generator-style production)

### Unit 10 — Dependency Injection *(Language: Java)*

- Dependency injection (build code from replaceable parts; makes testing + change safer)

### Unit 11 — Recursion *(Language: Java)*

- Recursion (define solutions in terms of smaller subproblems—sets you up for trees/DP)

### Unit 12 — Concurrency foundations *(Language: Java)*

- Threads vs async (two ways to overlap work)
- Race conditions (what goes wrong when timing matters)
- Locks (how to enforce safety, and why they can hurt performance)

---

## Course 3 — Data Structures & Algorithms (Java)

Goal: interview-ready fundamentals + practical instincts (complexity, tradeoffs, patterns).

### Unit 1 — Complexity basics *(Language: Java)*

- Big O (time and space intuition; “what grows with input size”)

### Unit 2 — Arrays and strings *(Language: Java)*

- Arrays and strings (indexing, slicing-like operations conceptually, common pitfalls)

### Unit 3 — Hashing + maps/sets *(Language: Java)*

- Hashing (why lookups can be fast, what collisions imply)
- Maps/Sets (membership, counting, grouping)

### Unit 4 — Stacks and queues *(Language: Java)*

- Stacks/Queues (LIFO/FIFO mental models)
- Monotonic stack/queue (pattern for “next greater”, “range min/max”, etc.)

### Unit 5 — Linked lists *(Language: Java)*

- Linked lists (pointer-style traversal; where they shine/fail)

### Unit 6 — Trees and heaps *(Language: Java)*

- Trees/Heaps (hierarchies, priority behavior)

### Unit 7 — Graph fundamentals *(Language: Java)*

- Graphs: BFS/DFS (reachability, traversal patterns)

### Unit 8 — Graph “workhorse” algorithms *(Language: Java)*

- Shortest path (Dijkstra)
- Topological sort (dependency ordering)

### Unit 9 — Sorting *(Language: Java)*

- Sorting (why it helps; when sort-first is the simplest win)

### Unit 10 — Searching *(Language: Java)*

- Searching (linear vs binary-search thinking)

### Unit 11 — Partitioning *(Language: Java)*

- Partitioning (split by predicate/pivot; key to many “in-place” approaches)

### Unit 12 — Core patterns *(Language: Java)*

- Two pointers
- Sliding window
- Intervals

### Unit 13 — Union-Find *(Language: Java)*

- Union-Find (connectivity / components problems)

### Unit 14 — Backtracking *(Language: Java)*

- Backtracking + pruning (systematic search with early exits)

### Unit 15 — Greedy thinking *(Language: Java)*

- Greedy + proof intuition (how to recognize when local choices are safe)

### Unit 16 — Dynamic programming *(Language: Java)*

- Dynamic programming (common patterns—state, transition, base cases—avoid “50 tricks”)

### Unit 17 — Bit manipulation (interview level) *(Language: Java)*

- Bit manipulation basics (masks, shifts—enough to solve common problems)

### Unit 18 — Complexity beyond Big-O *(Language: Java)*

- Amortized analysis (why some “expensive” operations average out)
- Space complexity tradeoffs (time vs memory)

---

## Course 4 — Computer Organization (Assembly + C)

Goal: understand what software is *actually doing* (memory, bits, execution model).

### Unit 1 — Bits and operations *(Language: Assembly concepts + C-adjacent)*

- Binary, bit manipulation, logical operations (now with “hardware-ish” meaning)

### Unit 2 — Digital logic (light) *(Language: Conceptual)*

- Digital logic (just enough context; don’t over-invest)

### Unit 3 — Memory layout *(Language: C + low-level model)*

- Memory layout: code, heap, stack, static (what lives where and why)

### Unit 4 — Assembly basics *(Language: Assembly)*

- Assembly (registers, basic instructions, reading tiny snippets to build intuition)

### Unit 5 — Manual memory management *(Language: C)*

- C — `malloc` (and the responsibility that comes with allocating memory)

---

## Course 5 — Git + Team Workflow Fundamentals (after Intro to Coding)

**Language/Tools:** Git + Shell/CLI (GitHub/GitLab concepts)

### Unit 1 — Git basics

- Working tree/stage/commit model; add/commit; push/pull; branches

### Unit 2 — PRs + code review

- PR essentials + review etiquette; keep PRs small; merge vs squash vs rebase (overview)

### Unit 3 — Rebase + history editing

- Rebase + interactive rebase (reword/squash/fixup); don’t rewrite shared history; reflog recovery

### Unit 4 — Merge + conflicts

- Merge vs rebase (when/why); resolve conflicts + rerun tests; reduce conflicts (sync early)

### Unit 5 — Daily team workflows

- Sync with main; commit hygiene; cherry-pick; revert vs reset

### Unit 6 — Debugging with Git

- Bisect; blame for context

### Unit 7 — Light release habits

- Tags/releases; backward-compatibility awareness

---

## Course 6 — OS Fundamentals (keep it light, but real)

Goal: understand the runtime environment your code depends on.

### Unit 1 — Concurrency at the OS level *(Language: Conceptual; ties to C/Java)*

- Processes vs threads (and *why it matters* operationally)

### Unit 2 — Virtual memory “what goes wrong” model *(Language: Conceptual)*

- Virtual memory basics (paging/page faults, stack/heap, debugging “memory weirdness”)

### Unit 3 — File descriptors + I/O behavior *(Language: Conceptual/Unix model)*

- File descriptors + basic I/O model (buffering, blocking vs non-blocking)

---

## Course 7 — Networking Fundamentals

Goal: be dangerous enough to build/debug real services.

### Unit 1 — The stack and packets *(Language: Conceptual)*

- Stack
- Packets (what’s actually moving around)

### Unit 2 — TCP vs UDP *(Language: Conceptual)*

- TCP vs UDP (reliability vs speed tradeoffs)

### Unit 3 — HTTP *(Language: Conceptual)*

- HTTP (requests/responses, headers, status codes as “contracts”)

### Unit 4 — Performance lens *(Language: Conceptual)*

- Latency vs throughput (how systems “feel fast” vs “handle load”)

---

## Course 8 — Engineering Craft: Debugging, Quality, APIs, Tests

Goal: write maintainable code like a mid-level SWE, not just “make it pass.”

### Unit 0 — Shell/CLI Productivity Basics *(Language/Tools: Unix shell — bash/zsh)*

- View output/files: `cat`, `less`, `head`, `tail`, `tail -f`
- Search text in logs/repos: `grep` (`n`, `i`, `r`)
- Compose commands: pipes `|`
- Save output: `>`, `>>`, `2>`
- Find files: `find`
- Batch apply commands: `xargs`
- Unstick processes: `ps`, `kill`
- Shell scripts: creating `.sh` files, shebang (`#!/bin/bash`), making executable with `chmod +x`, running with `./script.sh`
- Minimal env basics: PATH / “command not found”, one-off env vars (`VAR=value cmd`), and .shrc/.profile

### Unit 1 — Debugging fundamentals *(Language: Multi—Python/Java/TS mindset)*

- Debugging: logs, reproductions, bisection, instrumentation
    
    *(placed here because you now have enough surface area to debug real bugs)*
    

### Unit 2 — Code quality habits *(Language: Multi)*

- Quality: readability, naming, refactoring

### Unit 3 — Linting *(Language: Multi)*

- Linting (use it as “guard rails,” not a religion)

### Unit 4 — Documentation *(Language: Multi)*

- Documentation (how to explain intent, constraints, and pitfalls)

### Unit 5 — Codebase structure *(Language: Multi)*

- Modules (boundaries you can reason about)
- Dependency direction (keep “core” independent from “details”)
- Layering (UI → service → data, etc., with clean seams)

### Unit 6 — API design fundamentals *(Language: Multi; examples often Python/Java)*

- API design: clear contracts, validation, versioning, error semantics
- Pagination/filtering/sorting as first-class API concerns (because they affect clients forever)

### Unit 7 — Practical best practices *(Language: Multi)*

- Loose coupling
- DRY (and when repetition is actually clearer/safer)
- Avoid premature optimization
- “Build working → expand,” instead of designing the whole empire up front

### Unit 8 — Decorators / annotations *(Language: Python + Java)*

- Decorators/annotations (attach behavior/metadata without tangling core logic)

### Unit 9 — Testing strategy *(Language: Multi)*

- Unit vs integration vs e2e
- Mocks vs fakes
- Test boundaries + edge cases (what to mock, what to assert, what not to test)

---

## Course 9 — Backend Web Dev (Python: FastAPI + Django, plus DB/Cache/Queues)

Goal: ship and operate a real backend with good APIs, data, and reliability instincts.

### Unit 1 — HTTP/REST in practice *(Language: Python)*

- HTTP/REST fundamentals
- Middleware (cross-cutting behaviors: auth, logging, etc.)
- Auth: sessions vs JWT (tradeoffs + failure modes)

### Unit 2 — Building APIs with FastAPI/Django *(Language: Python)*

- FastAPI
- Django

### Unit 3 — Relational DB fundamentals *(Language: SQL + Python)*

- Database: relational fundamentals (Postgres)
- Schema design
- Indexes
- Migrations

### Unit 4 — ORM realism + performance intuition *(Language: Python + SQL)*

- ORMs vs raw SQL
- Query planning intuition (what “slow query” usually means)

### Unit 5 — Transactions and isolation *(Language: SQL + Python)*

- Transactions + isolation levels (dirty/non-repeatable/phantom read intuition)

### Unit 6 — Production database usage *(Language: Python + SQL)*

- Connection pooling (why it exists, common pitfalls)
- Pagination patterns (offset vs cursor)
- N+1 query problem (how to spot/fix)

### Unit 7 — Caching *(Language: Python + Redis concepts)*

- Caching: Redis basics
- Cache invalidation strategies

### Unit 8 — Async work *(Language: Python)*

- Background jobs/queues

### Unit 9 — Storage + integrations *(Language: Python)*

- File/object storage basics (S3/GCS concept + signed URLs)
- Webhooks (signature verification + retries)

### Unit 10 — Observability *(Language: Python)*

- Observability: structured logs, metrics, tracing basics

### Unit 11 — Security + robustness for real APIs *(Language: Python)*

- Security basics: OWASP top issues (practical level)
- Rate limiting + quotas
- Idempotency (esp. retries / payments-like operations)
- AuthN vs AuthZ, RBAC basics
- Secrets management basics (don’t ship secrets; rotation concept)
- Encryption vs hashing (when each applies)
- Secure logging (no secrets/PII)

---

## Course 10 — Frontend Web Dev (TypeScript + React)

Goal: build a modern UI that talks to your backend cleanly.

### Unit 1 — HTML *(Language: HTML)*

- HTML

### Unit 2 — CSS *(Language: CSS)*

- CSS

### Unit 3 — DOM + JavaScript *(Language: JavaScript)*

- DOM
- Javascript (how the browser executes your code)

### Unit 4 — TypeScript fundamentals *(Language: TypeScript)*

- Typescript (types as a tool to scale code safely)

### Unit 5 — React fundamentals *(Language: TypeScript + React)*

- React

### Unit 6 — Client-server interaction *(Language: TypeScript)*

- Ajax (fetching data from APIs)

### Unit 7 — Routing *(Language: TypeScript)*

- Routing

### Unit 8 — State and data fetching patterns *(Language: TypeScript)*

- State/data fetching patterns (server state vs UI state)

### Unit 9 — Tooling basics *(Language: TypeScript ecosystem)*

- Package manager + build tooling basics (npm/pnpm, “bundling” concept)

### Unit 10 — Styling systems *(Language: TypeScript + CSS utilities)*

- Tailwind? (only as a styling approach/tooling choice)

### Unit 11 — Frontend testing *(Language: TypeScript)*

- Frontend testing (component + e2e basics)

### Unit 12 — Accessibility basics *(Language: HTML/CSS/TS)*

- Accessibility basics (a11y)

---

## Course 11 — Systems Design Foundations

Goal: reason about scalable, reliable systems like an SD2 (not memorize diagrams).

### Unit 1 — Scaling primitives *(Language: Conceptual)*

- Load balancers
- Stateless services
- Caches
- CDNs

### Unit 2 — Storage tradeoffs *(Language: Conceptual)*

- SQL vs NoSQL
- Consistency models
- Replication basics

### Unit 3 — Async workflows *(Language: Conceptual)*

- Queues/streams
- Async workflows
- Idempotency (system-level necessity, not just an API detail)

### Unit 4 — Data distribution *(Language: Conceptual)*

- Partitioning/sharding concepts
- Hot keys

### Unit 5 — Reliability mechanics *(Language: Conceptual)*

- Retries
- Timeouts
- Circuit breakers
- Backpressure

### Unit 6 — Distributed systems practical realities *(Language: Conceptual)*

- At-least-once delivery + deduplication
- Eventual consistency intuition (stale reads, read-after-write expectations)
- Partial failures/timeouts as the default

### Unit 7 — Operating with targets *(Language: Conceptual)*

- SLOs
- Incident response basics

---

## Course 12 — Shipping & Operating Software (Infra + CI/CD + “Operate like an SD2”)

Goal: be able to deliver safely and own outcomes.

### Unit 1 — Containers *(Language: Docker)*

- Docker

### Unit 2 — Hosting fundamentals *(Language: Conceptual)*

- How to Host
- DBs (hosting/operating databases at a basic level)

### Unit 3 — Monitoring basics *(Language: Conceptual)*

- Logs
- Metrics
- Alerts

### Unit 4 — CI pipeline fundamentals *(Language: Conceptual)*

- CI pipeline fundamentals (lint/test/build)

### Unit 5 — Releases and rollbacks *(Language: Conceptual)*

- Release/rollback strategies (feature flags, canary/blue-green conceptually)
- Versioning/backward compatibility in deploys

### Unit 6 — Cloud/infra essentials *(Language: Conceptual vocabulary)*

- IAM/permissions basics (least privilege)
- VPC/security groups (what blocks traffic / “works locally” failures)
- Kubernetes concepts only (deployment/service/ingress vocabulary)

### Unit 7 — Operate like an SD2 *(Language: Multi; mostly process)*

- Design docs: requirements, tradeoffs, rollout plan, risks
- Incident basics: on-call triage, postmortems, action items
- Estimation + breaking down work + driving a project to completion