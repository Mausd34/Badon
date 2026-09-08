# Badon — Job-Ready Full-Stack Portfolio

Six deployable portfolio applications in one repository. Each project is designed with a clear separation between frontend/backend, environment configuration, tests, and production deployment guidance.

## Projects

1. AI Resume Analyzer — resume/job matching and skill-gap analysis.
2. Fraud Detection — transaction risk scoring and fraud analytics.
3. AI Customer Support — intent/FAQ support workflow with API-ready architecture.
4. Property & BPO Management — properties, vendors, work orders and SLA operations.
5. Blood Donation Platform — donor/request matching and city/blood-group filtering.
6. Inventory & POS — products, stock, cart, checkout and low-stock workflow.

## Deployment

### Local
- Python 3.12+
- Node.js 20+
- PostgreSQL 16+
- Create `.env` from `.env.example` where provided.
- Install backend dependencies and run migrations.
- Install frontend dependencies and run the Vite development server.

### Production
Recommended deployment: frontend on Vercel/Netlify and backend + PostgreSQL on Render/Railway/Fly.io. Set environment variables in the hosting provider; never commit secrets.

### CI/CD
GitHub Actions configuration validates Python syntax/tests and frontend builds on pushes and pull requests.

## Security
Use HTTPS, JWT/session authentication, CORS allowlists, server-side validation, database transactions, rate limiting and secure secret management before exposing services publicly.

## Portfolio note
These applications are educational/job-portfolio projects. Replace demo data and hard-coded examples with production integrations before real-world use.
