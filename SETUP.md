# COCO AI Global — starter project

This is a responsive visual starter, **not a live production website**. Login, wallet signing, database writes, token transfers, live prices and AI responses are not activated.

## Planned free-tier architecture
- Frontend: deploy on Vercel or Cloudflare Pages free tier.
- Authentication + database: Supabase free tier, with Row Level Security (RLS).
- Wallet connection: Reown AppKit / WalletConnect plus injected-wallet support.
- EVM networks: BNB Smart Chain, Ethereum, Polygon, Arbitrum, Base, Optimism and Avalanche.
- Admin role: assign only after verifying `Princesingh9634@gmail.com` through a trusted server-side process. Never trust a client-supplied email or role.

## Important security requirements
1. Never collect or store seed phrases, private keys, or wallet master passwords.
2. Wallet ownership must be verified using a signed, one-time nonce (SIWE/EIP-4361 or equivalent).
3. Protect all admin routes and database tables server-side. Hiding the admin page in the browser is not security.
4. Enable email verification, strong password policy, rate limiting, session expiry and 2FA for admin.
5. Use Supabase RLS policies so users can read/update only their own profile and records. Admin policies must be enforced server-side.
6. Never store API keys in frontend JavaScript. Use environment variables and server-side functions.
7. Deposits/withdrawals require audited contract logic, chain-specific confirmations, monitoring and explicit transaction signing. This starter does not move funds.

## Setup
1. Create a Supabase project and enable email/password authentication.
2. Create `profiles` and application tables; enable RLS on every user table.
3. Add a server-side owner bootstrap process to grant the admin role to the verified owner account. Do not allow public self-assignment of `admin`.
4. Create a Reown project and configure allowed origins for the production domain.
5. Integrate AppKit and test each wallet/network on testnets first.
6. Deploy this folder to Vercel or Cloudflare Pages. Add only public client config to frontend environment variables; keep service-role keys and secrets server-side.
7. Configure a custom domain only after the hosting deployment is verified.

## Existing COCO token reference
The earlier project discussion supplied BSC contract:
`0x5eca7e3da51ab758021c3765d147a7fcc7666666`

Verify the contract, token decimals, ownership, liquidity and audited source before enabling any token actions. Do not assume this address is verified or safe based solely on its presence here.
