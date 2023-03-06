## Encrypt OAuth Tokens using Evervault Outbound Relay

This is a demo to see how you can fully encrypt OAuth Tokens using Python and Evervault Outbound Relay.

## Getting Started

Create a virtual environment and install the required packages.

`python3 -m venv venv`

`source venv/bin/activate`

`pip3 install -r requirements.txt`

Open [http://localhost:5000](http://localhost:5000) with your browser to see the result.

The Github OAuth callback function can be edited in `app.py`.

The `pages/api` directory is mapped to `/api/*`. Files in this directory are treated as [API routes](https://nextjs.org/docs/api-routes/introduction) instead of React pages.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.


## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
