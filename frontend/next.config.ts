import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: process.env.NEXT_PUBLIC_IMAGE_DOMAIN!,
        pathname: '/**',
      },
    ],
  },
};

export default nextConfig;
