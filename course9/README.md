# Course 9: Backend Web Dev Fundamentals (FastAPI)

Learn backend development by building real APIs with FastAPI. Understand HTTP, databases, auth, caching, and production patterns through explicit hands-on code.

**For detailed course outline and exercise descriptions, see:** [../plans/course9/course-outline.md](../plans/course9/course-outline.md)

## Prerequisites

- **Course 1**: Python fundamentals (variables, control flow, functions, data structures)
- **Terminal basics**: running commands, navigating directories
- **Python environment**: pip, virtual environments
- **Conceptual understanding**: HTTP requests/responses from using web browsers

## Course Units

### Unit 1: HTTP/REST in Practice (45 min)
10 exercises teaching HTTP fundamentals, REST patterns, FastAPI basics, path/query parameters, request/response models, and automatic API docs.

### Unit 2: Middleware and Cross-Cutting Concerns (35 min)
8 exercises teaching middleware patterns, CORS, custom middleware, logging, timing, and dependency injection basics.

### Unit 3: Authentication and Authorization (50 min)
10 exercises teaching password hashing, sessions vs JWT, token creation/validation, OAuth2, route protection, and role-based access.

### Unit 4: Relational Databases with SQLAlchemy (50 min)
10 exercises teaching database fundamentals, SQLAlchemy models, relationships, CRUD operations, and schema design.

### Unit 5: Database Migrations with Alembic (35 min)
8 exercises teaching schema versioning, migration generation, rollback strategies, and data migrations.

### Unit 6: ORM Patterns and Performance (40 min)
9 exercises teaching query building, eager vs lazy loading, N+1 problem, and when to use raw SQL.

### Unit 7: Transactions and Isolation (35 min)
8 exercises teaching ACID properties, transaction boundaries, isolation levels, and locking strategies.

### Unit 8: Production Database Patterns (35 min)
8 exercises teaching connection pooling, pagination strategies, session management, and read replicas.

### Unit 9: Caching with Redis (40 min)
9 exercises teaching caching patterns, Redis data structures, TTL, cache invalidation, and when not to cache.

### Unit 10: Background Jobs and Queues (35 min)
8 exercises teaching async vs background jobs, task queues, retry patterns, and job monitoring.

### Unit 11: File Storage and Webhooks (40 min)
9 exercises teaching file uploads, object storage, signed URLs, webhook receiving, and webhook security.

### Unit 12: Observability (35 min)
8 exercises teaching structured logging, request tracing, metrics, health checks, and error tracking.

### Unit 13: API Security and Robustness (45 min)
10 exercises teaching OWASP Top 10, input validation, rate limiting, idempotency, RBAC, and secrets management.

### Final Project (90 min)
Build a production-ready API incorporating all course concepts: REST endpoints, auth, database, migrations, caching, background jobs, webhooks, logging, and security.

### Final Exam (30 min)

**Estimated Total Time:** 640 minutes (~10.5 hours)

## Setup

1. **Install PostgreSQL** (if not already installed):
   ```bash
   # macOS
   brew install postgresql@15
   brew services start postgresql@15
   
   # Create database
   createdb course9_db
   ```

2. **Install Redis** (if not already installed):
   ```bash
   # macOS
   brew install redis
   brew services start redis
   
   # Or use Docker
   docker run -d -p 6379:6379 redis:7-alpine
   ```

3. **Create virtual environment**:
   ```bash
   cd course9
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables** (create `.env` file in course9/):
   ```
   DATABASE_URL=postgresql://localhost/course9_db
   REDIS_URL=redis://localhost:6379
   SECRET_KEY=your-secret-key-change-this-in-production
   ```

## How to Use

1. Work through exercises in order within each unit
2. Run your code with `uvicorn` or `python` as indicated
3. Compare output to expected results
4. Take quiz (`quiz.yaml`) for self-reflection after each unit
5. Complete final project integrating all concepts
6. Take final exam (`final_exam.yaml`) after completing all units

## Running FastAPI Applications

Most exercises use FastAPI. Run them with:

```bash
uvicorn exercise_file:app --reload
```

Then visit `http://localhost:8000/docs` to see automatic API documentation.

## Tips

- Use the automatic `/docs` endpoint to test your APIs interactively
- Read error messages carefully—FastAPI gives helpful validation errors
- Use `print()` debugging liberally when learning
- Consult the cheat sheet when you forget syntax
- PostgreSQL and Redis must be running for database/cache exercises
