## Course 9 — Backend Web Dev Fundamentals (FastAPI)

Goal: learn backend concepts by building real APIs with FastAPI—explicit, hands-on, no magic.

### Unit 1 — HTTP/REST in practice *(Language: Python + FastAPI)*

- HTTP fundamentals: requests, responses, methods, status codes, headers
- REST patterns: resources, CRUD operations, URL design
- Build your first FastAPI endpoint: `@app.get()`, path parameters, query parameters
- Request/response models with Pydantic: type validation, automatic serialization
- Automatic OpenAPI docs: `/docs` and `/redoc` (understanding what good API docs look like)

### Unit 2 — Middleware and cross-cutting concerns *(Language: FastAPI)*

- What middleware is: functions that run before/after every request
- Built-in middleware: CORS, GZip compression, trusted hosts
- Custom middleware: logging requests, timing, adding request IDs
- Dependency injection basics: `Depends()` for shared logic (auth, DB connections)

### Unit 3 — Authentication and authorization *(Language: FastAPI)*

- Sessions vs JWT: stateful vs stateless auth (tradeoffs and failure modes)
- Implementing JWT auth: token creation, validation, expiration
- Password hashing with bcrypt/passlib (never store plaintext)
- OAuth2 with Password flow (FastAPI's security utilities)
- Protecting routes: dependencies for auth checking
- User context: getting the current user in route handlers

### Unit 4 — Relational databases with SQLAlchemy *(Language: SQL + Python)*

- Database fundamentals: tables, rows, columns, relationships (Postgres)
- SQLAlchemy Core vs ORM: when to use which
- Defining models: tables as Python classes, column types, constraints
- Relationships: one-to-many, many-to-many with foreign keys
- Basic CRUD operations: create, read, update, delete
- Schema design: normalization basics, when to denormalize

### Unit 5 — Database migrations with Alembic *(Language: Python + SQL)*

- What migrations are: version control for your database schema
- Alembic basics: `init`, `revision`, `upgrade`, `downgrade`
- Auto-generating migrations from model changes
- Writing custom migrations: data migrations, complex schema changes
- Rollback strategies: why migrations must be reversible

### Unit 6 — ORM patterns and performance *(Language: Python + SQL)*

- Query building: filters, joins, ordering, limiting
- Eager vs lazy loading: preventing N+1 queries
- `joinedload()`, `selectinload()`: explicit loading strategies
- When to drop to raw SQL: complex queries, performance optimization
- Query planning intuition: `EXPLAIN`, understanding slow queries

### Unit 7 — Transactions and isolation *(Language: SQL + Python)*

- What transactions are: atomic units of work (all-or-nothing)
- ACID properties: atomicity, consistency, isolation, durability
- Isolation levels: read uncommitted, read committed, repeatable read, serializable
- Dirty reads, non-repeatable reads, phantom reads (and why you care)
- Using transactions in FastAPI: session management, rollback on errors
- Optimistic vs pessimistic locking

### Unit 8 — Production database patterns *(Language: Python + SQL)*

- Connection pooling: why it exists, pool size tuning, connection exhaustion
- Pagination: offset-based vs cursor-based (and why offset is dangerous at scale)
- N+1 query problem: spotting it, fixing it with proper loading
- Database sessions in FastAPI: dependency injection for session management
- Read replicas: separating reads from writes (conceptually)

### Unit 9 — Caching with Redis *(Language: Python + Redis)*

- Why cache: reduce DB load, speed up reads
- Redis basics: key-value store, data types (strings, hashes, lists, sets)
- Cache patterns: cache-aside, write-through, write-behind
- Cache invalidation: time-based (TTL), event-based, manual
- Using Redis with FastAPI: dependency injection for Redis clients
- What not to cache: when caching makes things worse

### Unit 10 — Background jobs and queues *(Language: Python)*

- Async vs background jobs: when to use which
- Task queues: Celery or ARQ (pick one, learn the concepts)
- When to use background jobs: emails, reports, slow operations
- Job patterns: retry logic, exponential backoff, dead letter queues
- Monitoring jobs: tracking success/failure, alerting on stuck jobs

### Unit 11 — File storage and webhooks *(Language: Python)*

- Local storage vs object storage (S3/GCS)
- Uploading files in FastAPI: multipart form data, size limits
- Signed URLs: secure temporary access without credentials
- Webhooks: receiving events from external services
- Webhook security: signature verification (HMAC), replay protection
- Webhook reliability: retries, idempotency, timeouts

### Unit 12 — Observability *(Language: Python + FastAPI)*

- Structured logging: JSON logs, log levels, context
- Request tracing: correlation IDs across services
- Metrics basics: counters, gauges, histograms (Prometheus concepts)
- Health checks: `/health` endpoint, readiness vs liveness
- Error tracking: capturing exceptions, stack traces, context

### Unit 13 — API security and robustness *(Language: Python + FastAPI)*

- OWASP Top 10: SQL injection, XSS, CSRF, etc. (practical level)
- Input validation: Pydantic models catch bad data early
- Rate limiting: per-user, per-IP, sliding windows
- Idempotency keys: safe retries for critical operations (payments, etc.)
- AuthN vs AuthZ: who are you vs what can you do
- RBAC basics: roles, permissions, checking access
- Secrets management: environment variables, never commit secrets
- Encryption vs hashing: protecting data at rest vs verifying passwords
- Secure logging: never log secrets, tokens, or PII

---

## Course 9 Extended — Production Web Apps with Django

**Prerequisite:** Course 9 (FastAPI fundamentals)

Goal: learn how a batteries-included framework solves problems you now understand—and when to use it over FastAPI.

### Unit 1 — Django's philosophy vs FastAPI's *(Language: Django + Python)*

- Convention over configuration: Django's opinionated approach
- The "Django way": where things go, why the structure exists
- When to use Django: admin interfaces, rapid prototyping, traditional web apps
- When to use FastAPI: APIs, microservices, async-first, performance-critical
- Project setup: `django-admin startproject`, app structure
- Settings module: understanding Django's configuration system

### Unit 2 — Django ORM vs SQLAlchemy *(Language: Django)*

- Models: defining your schema with Django's ORM
- Migrations: `makemigrations`, `migrate` (comparison to Alembic)
- QuerySets: Django's query interface (lazy evaluation, chaining)
- Relationships: ForeignKey, ManyToMany, OneToOne
- The magic you now understand: how Django's ORM works under the hood
- When Django ORM shines: admin integration, simplicity
- When to use raw SQL: same rules as before, but Django makes it harder

### Unit 3 — Django's request/response cycle *(Language: Django)*

- MVT pattern: Model-View-Template (not MVC)
- URL routing: `urls.py`, path converters, URL patterns
- Views: function-based vs class-based views
- Request/response objects: what Django gives you
- Middleware: Django's version (global vs per-view)
- The request pipeline: understanding what happens on each request

### Unit 4 — Django Rest Framework (DRF) *(Language: Django + DRF)*

- Why DRF: building APIs the Django way
- Serializers: converting models to JSON (like Pydantic but heavier)
- ViewSets and Routers: automatic CRUD endpoints
- Permissions and authentication: DRF's built-in classes
- Comparison to FastAPI: when the magic helps, when it gets in the way
- Generic views: ListAPIView, CreateAPIView, etc.

### Unit 5 — Django Admin *(Language: Django)*

- The killer feature: automatic admin interface
- Registering models: `admin.site.register()`
- Customizing the admin: list_display, list_filter, search_fields
- Inline editing: managing related objects
- Custom actions: bulk operations
- When admin is worth it: internal tools, rapid CRUD interfaces
- When to skip it: public-facing apps, complex workflows

### Unit 6 — Django's auth system *(Language: Django)*

- Built-in User model: what you get for free
- Authentication backends: sessions, tokens
- Permissions and groups: Django's RBAC system
- Custom user models: when and how to extend
- Comparison to FastAPI JWT: sessions vs stateless tokens
- Django's password hashing: understanding the abstraction

### Unit 7 — Forms and validation *(Language: Django)*

- Django Forms: server-side form handling
- ModelForms: automatic forms from models
- Validation: clean methods, field validators
- CSRF protection: how Django handles it automatically
- When to use forms: server-rendered pages, admin interface
- When to skip forms: API-only backends (use DRF serializers)

### Unit 8 — Django templates (optional) *(Language: Django Template Language)*

- Template syntax: variables, filters, tags
- Template inheritance: base templates, blocks
- Context processors: global template variables
- Static files: CSS, JS, images
- When to use templates: traditional server-rendered apps
- When to skip them: API + React/Vue frontend (most modern apps)

### Unit 9 — Django best practices from a FastAPI perspective *(Language: Django)*

- Settings management: environment variables, django-environ
- Database connection pooling: pgbouncer, django-db-pool
- Avoiding N+1 queries: `select_related()`, `prefetch_related()` (same concepts, different API)
- Caching in Django: cache framework, view caching, template fragment caching
- Celery with Django: task queue integration (same concepts as FastAPI)
- Testing: Django TestCase vs pytest (and why pytest is still better)

### Unit 10 — Deployment and production patterns *(Language: Django)*

- WSGI vs ASGI: Django's deployment models
- Gunicorn/Uvicorn: serving Django in production
- Static file serving: WhiteNoise, CDN patterns
- Database migrations in production: zero-downtime strategies
- Django's check framework: `python manage.py check --deploy`
- Common pitfalls: DEBUG=False issues, static files, database connections

### Unit 11 — When to choose what *(Language: Conceptual)*

- FastAPI for: microservices, modern APIs, async-heavy workloads, explicit control
- Django for: monoliths, admin-heavy apps, rapid prototyping, "standard" web apps
- Framework fatigue: don't rewrite working code just to switch frameworks
- Mixing them: using FastAPI for API layer, Django for admin/background tasks (when it makes sense)
- The real lesson: understanding the tradeoffs, not religious framework wars