# E-Commerce Rebuild Project

This project is a full-stack modernization of my previous e-commerce platform, originally built with HTML, PHP, and CSS. It leverages Next.js for a fast, SEO-friendly, and dynamic frontend, paired with Django for a robust, scalable backend API.

Designed for a global audience, the platform will feature multi-language support, multi-currency transactions, and internationalization best practices to serve customers worldwide.

The architecture includes modern development standards such as Docker-based development, CI/CD pipelines, and production-ready deployment strategies, ensuring scalability, maintainability, and reliability.

Currently under active development, the final production-ready version will be hosted in a private GitLab repository.

## Progress / Roadmap

### Frontend
- [x] Setup Next.js frontend
- [ ] Pages
    - [ ] Main page
    - [ ] Product page
    - [ ] Search page
    - [ ] Blog page
    - [ ] User account page (login, register, profile)
    - [ ] Shopping and checkout
- [ ] Internationalization (country selection, language selection, dynamic urls)
- [ ] Chat AI integration
- [ ] Payment integration
- [ ] SEO optimization
- [ ] Analytics integration (Plausible)
- [ ] Testing (Cypress)

### Backend
- [x] Setup Django backend
- [ ] User authentication
    - [ ] Login, logout
    - [ ] Signup
    - [ ] Password reset
    - [ ] OAuth integration
- [ ] AI chat system
- [ ] Payment integration
- [ ] Background tasks (Celery)
- [ ] Testing (pytest)
- [x] Documentation (Swagger)
- [x] Integration with MinIO self-hosted-bucket

### Infrastructure / Production
- [x] Development docker setup
- [ ] Production docker setup
- [ ] Backup system
- [ ] Kubernetes setup
- [ ] CI/CD pipelines (GitLab)
- [ ] Monitoring & alerting

### Future Improvements / Possible Changes

These are ambitious features that may be considered in future iterations:
- Migration to Spring Boot or NestJS for the backend
- Full GraphQL API support for mobile apps
- Adoption of Onion Architecture for better modularity and testability
- Advanced Kubernetes HPA, Helm Charts
- Grafana, Prometheus, and ELK Stack
- Event-driven architecture and microservices decomposition

## License
Osk © All Rights Reserved
