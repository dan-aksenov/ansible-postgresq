# Ansible PostgreSQL install and serup role.
inspired by github.com/galaxyproject/ansible-postgresql

Variables are optional, or provided by defaults.

Designed to work no Centos7.

Features to be included:

- [x] Add repository,
- [x] Install postgres packages,
- [x] Initillize cluster if not exists,
   - [ ] Create default roles and databases,
- [x] Configure backups,
   - [x] Confiugre archivelog,
   - [x] backups with pgBackRest,
   - [ ] backups with barman (or not needed?),
- [x] Install Mamonsu and register in zabbix,
   - [ ] still need bootstrap and template import fix,
- [x] Install and configure pg_bouncer, 
   - [ ] Setup users and passwords. Get passwords dynamically from pg_shadow?
- [ ] Install usefull extensions,
   - [x] powa
- [ ] Configure pg_hba.conf,
- [x] Install tools,
- [x] Config for pgbadger logging and website,
- [x] Configure postgresql.conf
