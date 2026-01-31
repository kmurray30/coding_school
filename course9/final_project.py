# Course 9 Final Project: Production-Ready Task Management API
#
# Build a complete backend API for a task management system.
# This project integrates all concepts from the course.
#
# Your API must include:
# 
# 1. REST API DESIGN
#    - RESTful endpoints for tasks, users, projects
#    - Proper HTTP methods (GET, POST, PUT, DELETE)
#    - Appropriate status codes
#    - Request/response validation with Pydantic
#
# 2. AUTHENTICATION & AUTHORIZATION
#    - User registration and login
#    - JWT token authentication
#    - Password hashing with bcrypt
#    - Role-based access control (admin, user)
#    - Protected routes
#
# 3. DATABASE
#    - SQLAlchemy models for users, tasks, projects
#    - At least 3 related models (users, projects, tasks)
#    - One-to-many and many-to-many relationships
#    - Database migrations with Alembic
#    - Optimized queries (no N+1 problems)
#
# 4. CACHING
#    - Redis caching for expensive operations
#    - Cache project lists
#    - Cache user profiles
#    - Proper cache invalidation on updates
#
# 5. BACKGROUND JOBS
#    - Send email notifications (background task)
#    - Generate reports (background task)
#    - Task queue with retry logic
#
# 6. FILE HANDLING
#    - Upload task attachments
#    - File validation (size, type)
#    - Serve files securely
#
# 7. WEBHOOKS
#    - Receive webhooks for external integrations
#    - Send webhooks when tasks complete
#    - Signature verification
#    - Idempotency handling
#
# 8. OBSERVABILITY
#    - Structured JSON logging
#    - Correlation IDs for request tracing
#    - Health check endpoint
#    - Error tracking with context
#
# 9. SECURITY
#    - Input validation
#    - Rate limiting on auth endpoints
#    - No SQL injection
#    - Secrets in environment variables
#    - Security headers (CORS, etc.)
#    - Idempotency keys for critical operations
#
# 10. PRODUCTION PATTERNS
#     - Connection pooling
#     - Pagination (cursor-based for large datasets)
#     - Transaction handling
#     - Proper session management
#
# ============================================================
# DOMAIN MODEL
# ============================================================
#
# User:
#   - id, username, email, hashed_password, role
#   - Has many projects (as owner or member)
#   - Has many tasks (assigned)
#
# Project:
#   - id, name, description, owner_id
#   - Belongs to one user (owner)
#   - Has many tasks
#   - Has many members (users)
#
# Task:
#   - id, title, description, status, priority, due_date
#   - Belongs to one project
#   - Assigned to one user
#   - Has many attachments
#
# ============================================================
# REQUIRED FEATURES
# ============================================================
#
# User Management:
#   POST /register - Create new user
#   POST /login - Get JWT token
#   GET /me - Get current user profile (cached)
#   PUT /me - Update profile
#
# Project Management:
#   POST /projects - Create project (admin only)
#   GET /projects - List projects (cached, paginated)
#   GET /projects/{id} - Get project details
#   PUT /projects/{id} - Update project (owner only)
#   DELETE /projects/{id} - Delete project (owner only)
#   POST /projects/{id}/members - Add member
#
# Task Management:
#   POST /projects/{project_id}/tasks - Create task
#   GET /projects/{project_id}/tasks - List tasks (paginated)
#   GET /tasks/{id} - Get task details
#   PUT /tasks/{id} - Update task
#   DELETE /tasks/{id} - Delete task
#   POST /tasks/{id}/assign - Assign to user
#   POST /tasks/{id}/complete - Mark complete (sends webhook)
#
# File Management:
#   POST /tasks/{id}/attachments - Upload file
#   GET /tasks/{id}/attachments - List attachments
#   GET /attachments/{id} - Download file
#
# Webhooks:
#   POST /webhooks/task-updated - Receive external updates
#   (Your API sends webhooks when tasks complete)
#
# Observability:
#   GET /health - Health check
#   GET /metrics - Basic metrics
#
# ============================================================
# EVALUATION CRITERIA
# ============================================================
#
# Your project will be evaluated on:
#
# 1. Completeness
#    - All required features implemented
#    - API is functional and testable
#
# 2. Code Quality
#    - Clean, readable code
#    - Proper error handling
#    - No hardcoded values
#
# 3. Security
#    - Authentication works correctly
#    - Authorization checks on protected endpoints
#    - Input validation
#    - No security vulnerabilities
#
# 4. Performance
#    - Caching reduces database load
#    - No N+1 query problems
#    - Efficient pagination
#
# 5. Production Readiness
#    - Logging for debugging
#    - Health checks
#    - Error tracking
#    - Proper configuration
#
# ============================================================
# GETTING STARTED
# ============================================================
#
# 1. Plan your database schema
# 2. Set up Alembic for migrations
# 3. Create your models
# 4. Build authentication first
# 5. Add endpoints incrementally
# 6. Test as you go (use /docs)
# 7. Add caching, background jobs, webhooks
# 8. Add observability and security features
#
# You choose:
# - File structure
# - Additional features
# - Data models (extend as needed)
# - API response formats
# - Caching strategy
#
# Make it production-ready. Pretend you're building this for a real company.
# 
# ============================================================
# DELIVERABLES
# ============================================================
#
# 1. Working FastAPI application
# 2. README with setup instructions
# 3. Alembic migrations
# 4. requirements.txt with dependencies
# 5. .env.example with required environment variables
# 6. API is testable via /docs
#
# No scaffolding provided. Build it from scratch.
# You have all the knowledge from this course.
# 
# Good luck!

# Start here:
from fastapi import FastAPI

app = FastAPI(title="Task Management API")

# Your implementation...
