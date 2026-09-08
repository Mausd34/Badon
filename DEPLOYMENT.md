# Multi-stage deployment guide

## 1. Prepare
Clone the repository, choose a project, and create its environment file from `.env.example` when present. Install dependencies in the project's backend and frontend directories.

## 2. Database
Use PostgreSQL in production. Run the project's migrations/initialization before starting the API.

## 3. Backend
Set `DEBUG=false`, a strong random `SECRET_KEY`, production `DATABASE_URL`, and an exact `CORS_ORIGINS` list. Start the API with a production ASGI/WSGI server appropriate to the selected backend.

## 4. Frontend
Set `VITE_API_URL` to the deployed backend URL, install dependencies with `npm ci`, and run `npm run build`. Serve the generated `dist` directory through the hosting provider/CDN.

## 5. Hosting
Frontend: Vercel or Netlify. Backend: Render, Railway or Fly.io. Database: managed PostgreSQL from the backend provider or another managed service.

## 6. Domain/HTTPS
Attach a custom domain and enable HTTPS. Configure CORS and trusted hosts to the final domains only.

## 7. Secrets
Do not commit `.env`, API keys, JWT secrets, database passwords or private credentials. Add secrets through the hosting provider/GitHub Actions secret store.

## 8. Verification
After deployment test: health endpoint, login/auth, CRUD, database writes, file uploads if applicable, frontend API connectivity, mobile layout and error handling.
