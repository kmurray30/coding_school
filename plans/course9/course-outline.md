# Course 9 Outline: Backend Web Dev Fundamentals (FastAPI)

## Prerequisites

- **Course 1**: Python fundamentals (variables, control flow, functions, data structures)
- **Basic terminal usage**: running commands, navigating directories
- **Python environment setup**: pip, virtual environments
- **Understanding of requests/responses** from using web browsers (conceptual level)

## Course Overview

This course teaches backend web development through FastAPI. Students learn HTTP, REST APIs, databases, authentication, caching, and production patterns by building real APIs with explicit code—no magic frameworks hiding the details.

**Key Philosophy:** Understand the concepts first (FastAPI), then recognize when batteries-included frameworks help (Django extended course).

---

## Unit 1: HTTP/REST in Practice

**Core Concepts:** HTTP request/response cycle, REST patterns, FastAPI basics, Pydantic validation

**Exercise Count:** 10 exercises

**Exercises:**

1. **exercise1_first_endpoint** - [Observation] Complete FastAPI app with one GET endpoint. Run and see the response in browser. Introduces `@app.get()`, uvicorn, and automatic JSON serialization.

2. **exercise2_status_codes** - [Observation] Working endpoints that return different status codes (200, 404, 201). Demonstrates HTTP status code meanings by running and testing.

3. **exercise3_path_parameters** - [Guided] Modify endpoint to accept path parameters (`/users/{user_id}`). Fill in the parameter extraction and return user info.

4. **exercise4_query_parameters** - [Guided] Add query parameters to filter results (`/items?category=books&limit=10`). Shows URL structure and optional parameters.

5. **exercise5_http_methods** - [Semi-independent] Implement POST, PUT, DELETE endpoints for a resource. Students write CRUD operations from descriptions.

6. **exercise6_request_bodies** - [Semi-independent] Accept JSON request bodies and validate them. Introduces raw Pydantic models without scaffolding.

7. **exercise7_response_models** - [Semi-independent] Define response models with Pydantic. Ensure API returns consistent, typed responses.

8. **exercise8_api_docs** - [Observation] Explore `/docs` and `/redoc`. Understand automatic OpenAPI documentation and why it matters.

9. **exercise9_rest_resource_design** - [Challenge] Design a RESTful API for a blog (posts, comments). Students choose URL patterns and methods following REST conventions.

10. **exercise10_simple_api** - [Project-scale] Build a small API for managing a personal library (books, authors, reading status). Combine all concepts: routes, methods, path/query params, request/response models, proper status codes.

**Quiz Topics:**
- HTTP methods and when to use each (GET, POST, PUT, DELETE)
- Status codes: 2xx, 3xx, 4xx, 5xx categories and common codes
- Path parameters vs query parameters
- REST resource design principles
- Pydantic model validation basics
- Where to find API documentation in FastAPI

---

## Unit 2: Middleware and Cross-Cutting Concerns

**Core Concepts:** Middleware pattern, CORS, custom middleware, dependency injection basics

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_cors_middleware** - [Observation] Complete app with CORS middleware configured. Test from browser console to see CORS headers.

2. **exercise2_logging_middleware** - [Observation] Middleware that logs every request with timestamp, path, method. Run and observe logs.

3. **exercise3_timing_middleware** - [Guided] Add timing to middleware—log how long each request takes. Fill in time calculation logic.

4. **exercise4_custom_headers** - [Guided] Middleware that adds custom headers (request ID, server version) to every response.

5. **exercise5_request_context** - [Semi-independent] Create middleware that generates unique request IDs and attaches them to request state.

6. **exercise6_simple_dependency** - [Semi-independent] Write a dependency function using `Depends()` for shared logic (e.g., getting current timestamp).

7. **exercise7_chained_dependencies** - [Challenge] Create dependencies that depend on other dependencies. Demonstrates dependency injection composition.

8. **exercise8_api_with_middleware** - [Project-scale] Build an API with multiple middleware layers: CORS, request logging, timing, custom error formatting. Students choose what middleware to implement for their use case.

**Quiz Topics:**
- What middleware does and when to use it
- CORS: what it is and why it exists
- Difference between middleware and dependencies
- Execution order of middleware
- Common use cases for custom middleware
- How `Depends()` works in FastAPI

---

## Unit 3: Authentication and Authorization

**Core Concepts:** Sessions vs JWT, password hashing, OAuth2, route protection, user context

**Exercise Count:** 10 exercises

**Exercises:**

1. **exercise1_password_hashing** - [Observation] Complete code showing bcrypt hashing and verification. Hash a password and verify it works.

2. **exercise2_sessions_vs_jwt** - [Observation] Text/conceptual exercise explaining tradeoffs. Read scenarios and identify when to use each.

3. **exercise3_create_jwt** - [Guided] Generate a JWT token with user data and expiration. Fill in claims and signing logic.

4. **exercise4_verify_jwt** - [Guided] Decode and validate a JWT token. Handle expiration and invalid signatures.

5. **exercise5_login_endpoint** - [Semi-independent] Build a `/login` endpoint that accepts username/password, verifies them, and returns a JWT.

6. **exercise6_protected_route** - [Semi-independent] Create a route that requires a valid JWT in the Authorization header. Return 401 if missing/invalid.

7. **exercise7_get_current_user** - [Semi-independent] Write a dependency that extracts the current user from the JWT token. Use `Depends()` to inject it into routes.

8. **exercise8_oauth2_password** - [Challenge] Implement OAuth2 with Password flow using FastAPI's security utilities. Includes token endpoint and bearer scheme.

9. **exercise9_role_based_access** - [Challenge] Add roles (admin, user) and protect routes based on role. Implement authorization checks beyond authentication.

10. **exercise10_auth_system** - [Project-scale] Build a complete auth system: user registration (with password hashing), login (returns JWT), protected routes (user must be logged in), user profile endpoint (returns current user info). No scaffolding—students design the flow.

**Quiz Topics:**
- Difference between authentication and authorization
- Sessions vs JWT: tradeoffs and when to use each
- Why you never store plaintext passwords
- How JWT tokens work (claims, signing, expiration)
- OAuth2 Password flow basics
- HTTP status codes for auth failures (401 vs 403)
- What goes in the Authorization header

---

## Unit 4: Relational Databases with SQLAlchemy

**Core Concepts:** Tables, relationships, SQLAlchemy ORM, schema design, CRUD operations

**Exercise Count:** 10 exercises

**Exercises:**

1. **exercise1_database_basics** - [Observation] Text exercise explaining tables, rows, columns, and why relational databases exist. Conceptual foundation.

2. **exercise2_sqlalchemy_model** - [Observation] Complete SQLAlchemy model definition. Run to create a table and insert a row.

3. **exercise3_column_types** - [Guided] Define a model with various column types (String, Integer, DateTime, Boolean). Create and query records.

4. **exercise4_constraints** - [Guided] Add constraints to models: unique, nullable, default values. Observe what happens when you violate them.

5. **exercise5_one_to_many** - [Semi-independent] Create a one-to-many relationship (User → Posts). Define the relationship using `relationship()` and ForeignKey.

6. **exercise6_many_to_many** - [Semi-independent] Create a many-to-many relationship (Students ↔ Courses) using an association table.

7. **exercise7_crud_operations** - [Semi-independent] Implement create, read, update, delete operations for a model. Students write the SQLAlchemy session code.

8. **exercise8_normalization** - [Observation] Text/conceptual exercise showing normalized vs denormalized schemas. Identify when to normalize and when not to.

9. **exercise9_schema_design** - [Challenge] Design a database schema for an e-commerce system (products, orders, customers). Students create models with appropriate relationships.

10. **exercise10_fastapi_database** - [Project-scale] Integrate SQLAlchemy with FastAPI. Build an API with database-backed CRUD endpoints (e.g., blog posts API with database persistence). Include session management as a dependency.

**Quiz Topics:**
- What relational databases are and when to use them
- Tables, rows, columns, relationships
- Primary keys and foreign keys
- One-to-many vs many-to-many relationships
- SQLAlchemy Core vs ORM
- Basic CRUD operations
- Normalization basics

---

## Unit 5: Database Migrations with Alembic

**Core Concepts:** Schema versioning, migration scripts, auto-generation, rollback strategies

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_why_migrations** - [Observation] Text exercise explaining why migrations exist. Scenarios showing problems without version control for schema.

2. **exercise2_alembic_init** - [Guided] Initialize Alembic in a project. Run `alembic init` and configure connection string.

3. **exercise3_first_migration** - [Guided] Create the first migration from existing models using `alembic revision --autogenerate`. Run `alembic upgrade head`.

4. **exercise4_add_column** - [Semi-independent] Add a new column to a model and generate a migration. Apply it and verify the column exists.

5. **exercise5_data_migration** - [Semi-independent] Write a custom migration that updates existing data (not just schema). Populate default values for a new column.

6. **exercise6_rollback** - [Semi-independent] Downgrade a migration using `alembic downgrade -1`. Understand why migrations must be reversible.

7. **exercise7_complex_migration** - [Challenge] Handle a breaking schema change (renaming a column, splitting a table). Write a multi-step migration.

8. **exercise8_migration_workflow** - [Project-scale] Evolve a database schema over time. Start with a simple model, add features through migrations (new tables, relationships, constraints). Practice the full workflow: change model → generate migration → review → apply → test.

**Quiz Topics:**
- What database migrations are and why they're needed
- Alembic commands: init, revision, upgrade, downgrade
- Auto-generation vs manual migrations
- Why migrations should be reversible
- How to handle data migrations
- Rollback strategies

---

## Unit 6: ORM Patterns and Performance

**Core Concepts:** Query building, eager vs lazy loading, N+1 problem, raw SQL

**Exercise Count:** 9 exercises

**Exercises:**

1. **exercise1_query_basics** - [Observation] Complete code showing filters, ordering, limiting with SQLAlchemy. Run and see results.

2. **exercise2_joins** - [Observation] Query with explicit joins. Demonstrates how to access related data.

3. **exercise3_lazy_loading** - [Observation] Code that triggers lazy loading. Count the SQL queries (N+1 problem). See the performance issue firsthand.

4. **exercise4_eager_loading** - [Guided] Fix the N+1 problem using `joinedload()`. Compare query counts before and after.

5. **exercise5_selectinload** - [Guided] Use `selectinload()` for collections. Understand when to use it vs `joinedload()`.

6. **exercise6_complex_filters** - [Semi-independent] Build queries with multiple filters, sorting, pagination. Students write the query chain.

7. **exercise7_raw_sql** - [Semi-independent] Write a complex query using raw SQL when ORM gets awkward. Use `session.execute()`.

8. **exercise8_query_planning** - [Observation] Use `EXPLAIN` to understand query performance. See indexes in action (or lack thereof).

9. **exercise9_optimized_api** - [Project-scale] Build an API endpoint with complex queries. Optimize for performance using appropriate loading strategies. Students choose the right approach for their data access patterns.

**Quiz Topics:**
- Eager vs lazy loading
- N+1 query problem and how to spot it
- `joinedload()` vs `selectinload()`
- When to use raw SQL instead of ORM
- Query planning basics
- Performance implications of loading strategies

---

## Unit 7: Transactions and Isolation

**Core Concepts:** ACID properties, transaction boundaries, isolation levels, locking

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_acid_properties** - [Observation] Text exercise explaining atomicity, consistency, isolation, durability with real-world examples.

2. **exercise2_simple_transaction** - [Observation] Complete code showing a transaction with commit/rollback. Run and see the all-or-nothing behavior.

3. **exercise3_rollback_on_error** - [Guided] Transaction that rolls back on exception. Fill in error handling and rollback logic.

4. **exercise4_isolation_levels** - [Observation] Text/conceptual exercise explaining isolation levels and their tradeoffs.

5. **exercise5_dirty_reads** - [Guided] Demonstrate a dirty read scenario. Show why isolation levels matter.

6. **exercise6_transaction_fastapi** - [Semi-independent] Integrate transactions with FastAPI endpoints. Use dependency injection for session management with auto-rollback on errors.

7. **exercise7_optimistic_locking** - [Challenge] Implement optimistic locking with version numbers. Handle concurrent updates gracefully.

8. **exercise8_money_transfer** - [Project-scale] Build a money transfer API that uses transactions correctly. Ensure atomic transfers: debit one account, credit another, rollback if anything fails. Handle race conditions with appropriate isolation or locking.

**Quiz Topics:**
- ACID properties and what each means
- What transactions are and when to use them
- Isolation levels: read uncommitted, read committed, repeatable read, serializable
- Dirty reads, non-repeatable reads, phantom reads
- Optimistic vs pessimistic locking
- Using transactions in FastAPI

---

## Unit 8: Production Database Patterns

**Core Concepts:** Connection pooling, pagination, session management, read replicas

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_connection_pooling** - [Observation] Text exercise explaining connection pooling, pool exhaustion, and tuning. Conceptual understanding.

2. **exercise2_offset_pagination** - [Guided] Implement offset-based pagination (`LIMIT`/`OFFSET`). See it in action.

3. **exercise3_cursor_pagination** - [Guided] Implement cursor-based pagination (using `id >` or timestamps). Compare to offset-based.

4. **exercise4_pagination_tradeoffs** - [Observation] Text exercise on offset vs cursor pagination at scale. Understand when each breaks down.

5. **exercise5_n_plus_one_detection** - [Semi-independent] Given an API endpoint, identify the N+1 query problem and fix it. Students debug and optimize.

6. **exercise6_session_dependency** - [Semi-independent] Create a FastAPI dependency for database session management. Ensure proper session cleanup.

7. **exercise7_read_replicas** - [Observation] Text/conceptual exercise on read replicas. When to use them, how to route reads vs writes (conceptual only, no actual replica setup).

8. **exercise8_production_api** - [Project-scale] Build a production-ready API with proper session management, pagination, connection pooling configuration, and optimized queries. Students make architectural decisions about how to structure database access.

**Quiz Topics:**
- Connection pooling: what it is and why it matters
- Pool size tuning considerations
- Offset vs cursor pagination
- N+1 query problem (again, because it's that important)
- Session management best practices in FastAPI
- Read replicas: when and why

---

## Unit 9: Caching with Redis

**Core Concepts:** Caching patterns, Redis data structures, TTL, cache invalidation

**Exercise Count:** 9 exercises

**Exercises:**

1. **exercise1_why_cache** - [Observation] Text exercise showing scenarios where caching helps and where it hurts. Build intuition.

2. **exercise2_redis_basics** - [Observation] Complete code using Redis: set, get, delete. Run and see key-value storage in action.

3. **exercise3_ttl** - [Guided] Set TTL (time-to-live) on cache entries. Verify they expire automatically.

4. **exercise4_cache_aside** - [Guided] Implement cache-aside pattern: check cache, if miss fetch from DB and cache it.

5. **exercise5_redis_data_types** - [Semi-independent] Use Redis hashes, lists, or sets. Students choose appropriate data structure for their use case.

6. **exercise6_cache_invalidation** - [Semi-independent] Invalidate cache when data changes. Update DB and delete cache key.

7. **exercise7_cache_dependency** - [Semi-independent] Create FastAPI dependency for Redis client. Inject it into routes.

8. **exercise8_when_not_to_cache** - [Observation] Text exercise on anti-patterns. Identify scenarios where caching makes things worse (stale data problems, cache stampede).

9. **exercise9_cached_api** - [Project-scale] Add caching to an existing API. Cache expensive queries, implement proper invalidation, handle cache misses gracefully. Students decide what to cache and for how long.

**Quiz Topics:**
- Why caching exists and when to use it
- Cache-aside vs write-through vs write-behind
- TTL and cache expiration
- Cache invalidation strategies
- Redis data types and when to use each
- When caching is the wrong solution

---

## Unit 10: Background Jobs and Queues

**Core Concepts:** Async vs background jobs, task queues, retry patterns, monitoring

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_async_vs_background** - [Observation] Text exercise explaining when to use async (I/O-bound) vs background jobs (long-running, out-of-band).

2. **exercise2_simple_task** - [Observation] Complete background task with Celery or ARQ. Run and see it execute asynchronously.

3. **exercise3_retry_logic** - [Guided] Add retry logic to a task that might fail. Configure max retries and exponential backoff.

4. **exercise4_task_from_api** - [Guided] Trigger a background job from a FastAPI endpoint. Return immediately with task ID.

5. **exercise5_task_status** - [Semi-independent] Check task status (pending, running, complete, failed). Build an endpoint to poll status.

6. **exercise6_dead_letter_queue** - [Semi-independent] Handle permanently failed tasks. Send them to a dead letter queue for manual inspection.

7. **exercise7_task_patterns** - [Challenge] Implement common patterns: sending emails, generating reports, processing uploads. Students choose which to background.

8. **exercise8_job_system** - [Project-scale] Build an API with background job processing. Example: file processing (upload returns immediately, background job processes file, status endpoint shows progress). Include retry logic and error handling.

**Quiz Topics:**
- Async vs background jobs: when to use which
- Task queue concepts
- Retry logic and exponential backoff
- Dead letter queues
- Common use cases for background jobs
- Monitoring job success/failure

---

## Unit 11: File Storage and Webhooks

**Core Concepts:** File uploads, object storage, signed URLs, webhook receiving and security

**Exercise Count:** 9 exercises

**Exercises:**

1. **exercise1_file_upload** - [Observation] Complete FastAPI endpoint accepting file upload. Save to disk and return confirmation.

2. **exercise2_file_validation** - [Guided] Validate file size and type. Reject files that are too large or wrong format.

3. **exercise3_object_storage** - [Observation] Text exercise explaining local storage vs S3/GCS. Tradeoffs and when to use each.

4. **exercise4_signed_urls** - [Guided] Generate a signed URL for temporary file access. Understand security implications.

5. **exercise5_webhook_endpoint** - [Semi-independent] Create an endpoint that receives webhook payloads. Parse and log the event.

6. **exercise6_webhook_signature** - [Semi-independent] Verify webhook signatures using HMAC. Reject tampered requests.

7. **exercise7_idempotency** - [Semi-independent] Handle duplicate webhook deliveries with idempotency keys. Process each event exactly once.

8. **exercise8_webhook_retry** - [Challenge] Handle webhook timeouts and retries. Implement exponential backoff for failed webhooks you send.

9. **exercise9_file_webhook_system** - [Project-scale] Build a system that accepts file uploads and sends webhooks when processing completes. Include signature verification for incoming webhooks, signed URLs for file download, and idempotency handling.

**Quiz Topics:**
- Local storage vs object storage (S3/GCS)
- File upload validation and security
- Signed URLs and temporary access
- What webhooks are and when to use them
- Webhook signature verification (HMAC)
- Idempotency and replay protection

---

## Unit 12: Observability

**Core Concepts:** Structured logging, request tracing, metrics, health checks, error tracking

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_structured_logging** - [Observation] Complete code with JSON structured logging. See log levels and context in action.

2. **exercise2_log_levels** - [Guided] Use appropriate log levels (DEBUG, INFO, WARNING, ERROR). Students categorize different events.

3. **exercise3_correlation_ids** - [Guided] Add correlation/request IDs to logs. Trace a single request across multiple log entries.

4. **exercise4_metrics_basics** - [Observation] Text exercise explaining counters, gauges, histograms. Prometheus concepts at high level.

5. **exercise5_health_check** - [Semi-independent] Implement `/health` endpoint that checks database connectivity and returns status.

6. **exercise6_readiness_liveness** - [Semi-independent] Understand readiness vs liveness probes. Implement both for Kubernetes-style deployments.

7. **exercise7_error_tracking** - [Semi-independent] Capture exceptions with context (user, request ID, stack trace) for error tracking services.

8. **exercise8_observable_api** - [Project-scale] Add full observability to an API: structured logging with correlation IDs, health checks, error tracking, request timing logs. Students instrument their application properly.

**Quiz Topics:**
- Structured logging vs unstructured
- Log levels and when to use each
- Correlation IDs and request tracing
- Metrics: counters, gauges, histograms
- Health checks: readiness vs liveness
- What to include in error tracking

---

## Unit 13: API Security and Robustness

**Core Concepts:** Input validation, rate limiting, idempotency, RBAC, secrets management, OWASP Top 10

**Exercise Count:** 10 exercises

**Exercises:**

1. **exercise1_owasp_top_10** - [Observation] Text exercise covering OWASP Top 10 at practical level. SQL injection, XSS, CSRF examples.

2. **exercise2_input_validation** - [Observation] See Pydantic models catch invalid data. Run examples with bad input and see validation errors.

3. **exercise3_sql_injection** - [Guided] Show vulnerable code and how parameterized queries (SQLAlchemy) prevent SQL injection.

4. **exercise4_rate_limiting** - [Guided] Implement basic rate limiting (per-IP or per-user). Reject requests that exceed limit.

5. **exercise5_idempotency_keys** - [Semi-independent] Handle idempotency keys for critical operations (payments). Ensure safe retries.

6. **exercise6_authn_authz** - [Observation] Text exercise reinforcing authentication vs authorization. Who you are vs what you can do.

7. **exercise7_rbac** - [Semi-independent] Implement role-based access control. Check user roles before allowing operations.

8. **exercise8_secrets_management** - [Semi-independent] Use environment variables for secrets. Never commit credentials. Load secrets at runtime.

9. **exercise9_encryption_vs_hashing** - [Observation] Text exercise explaining when to encrypt (data at rest) vs hash (passwords, verification).

10. **exercise10_secure_api** - [Project-scale] Build a security-hardened API. Include: input validation, rate limiting, role-based access, proper auth, no secrets in code, secure logging (no PII/tokens). Students make security decisions and implement defenses.

**Quiz Topics:**
- OWASP Top 10 highlights
- SQL injection and how to prevent it
- XSS, CSRF basics
- Input validation importance
- Rate limiting strategies
- Idempotency keys for safe retries
- Authentication vs authorization
- RBAC: roles and permissions
- Secrets management best practices
- Encryption vs hashing

---

## Final Project

**Scope:** Build a complete backend API incorporating all course concepts.

**Description:**

Build a production-ready API for a domain of your choice. Examples: task management, social media, e-commerce, booking system, etc.

Your API must include:
- RESTful endpoints with proper HTTP methods and status codes
- Request/response validation with Pydantic
- JWT authentication (registration, login, protected routes)
- Database integration with SQLAlchemy (at least 3 related models)
- Database migrations with Alembic
- At least one optimized query (proper loading strategy)
- Redis caching for expensive operations
- Background job for a long-running task
- Webhook endpoint (receive external events)
- Structured logging with correlation IDs
- Health check endpoint
- Rate limiting on sensitive endpoints
- Input validation and basic security practices

You choose the domain, the models, and the features. Make it something you'd actually want to use. The API should feel production-ready—not a toy.

**Expected deliverables:** Working FastAPI application with all features implemented, README with setup instructions, and clear API documentation (via `/docs`).

---

## Final Exam

**Coverage:** All 13 units, cumulative review of backend development concepts

**Question Count:** ~50-60 questions

**Focus Areas:**
- HTTP fundamentals and REST design
- Middleware and dependency injection patterns
- Authentication and authorization (sessions, JWT, OAuth2)
- Database modeling and relationships
- SQLAlchemy ORM queries and optimization
- Database migrations and schema evolution
- ACID properties and transactions
- Isolation levels and concurrency
- Connection pooling and session management
- Pagination strategies
- Caching patterns and invalidation
- Redis data structures
- Background jobs and task queues
- File storage and webhooks
- Webhook security (signatures, idempotency)
- Observability (logging, metrics, health checks)
- OWASP Top 10 and common vulnerabilities
- Rate limiting and idempotency
- RBAC and authorization patterns
- Secrets management
- When to use each pattern/technology (conceptual decision-making)

---

## Notes on Pacing

- **Early units (1-3):** Build foundation with FastAPI, HTTP, middleware, auth. More observation exercises.
- **Mid units (4-8):** Database-heavy units. Students should be comfortable writing code by now—more semi-independent exercises.
- **Late units (9-13):** Production patterns. Emphasize decision-making and tradeoffs. Challenge exercises that combine multiple concepts.
- **Final project:** Integrates everything. Students should feel accomplished building a real API from scratch.

## External Dependencies

- **FastAPI** (web framework)
- **Uvicorn** (ASGI server)
- **SQLAlchemy** (ORM)
- **Alembic** (migrations)
- **PostgreSQL** (database—students should have it installed)
- **Redis** (caching—students should have it installed or use Docker)
- **Pydantic** (comes with FastAPI)
- **python-jose[cryptography]** (JWT)
- **passlib[bcrypt]** (password hashing)
- **Celery or ARQ** (background jobs—pick one for consistency)
- **python-multipart** (file uploads)

Include a `requirements.txt` in the course directory with pinned versions.

## Setup Instructions

Students should set up:
1. Python virtual environment
2. PostgreSQL database (local or Docker)
3. Redis server (local or Docker)
4. Install dependencies from `requirements.txt`
5. Run initial Alembic migrations
6. Start uvicorn server

Provide clear setup instructions in course README.
