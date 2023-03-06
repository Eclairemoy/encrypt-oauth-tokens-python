## Encrypt OAuth Tokens using Evervault Outbound Relay

This is a demo to see how you can fully encrypt OAuth Tokens using Python and Evervault Outbound Relay.

## Getting Started

Create a virtual environment and install the required packages.

`python3 -m venv venv`

`source venv/bin/activate`

`pip3 install -r requirements.txt`

Open [http://localhost:5000](http://localhost:5000) with your browser to see the result.

The Github OAuth callback function can be edited in `app.py`.

After you have created your Github OAuth app, go to `https://github.com/login/oauth/authorize?scope=user:email&client_id=` + `YOUR_GITHUB_CLIENT_ID` in your browser to initiate the Authorization flow.

## Learn More

To learn more about Evervault check out:

- [Evervault Python SDK](https://docs.evervault.com/sdks/reactjs)
- [Evervault Outbound Relay](https://docs.evervault.com/sdks/nodejs)

