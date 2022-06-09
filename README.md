Rework of upstream https://github.com/tv-vicomtech/SPARTA_JCCI_NODE


Check `docker-compose.yml` for default expected values as documented or set in
the upstream project

The following variables need to be updated in the compose file

Provided by the JCCI team - check upstream README file for people at VicomTech:

- `PEP_PROXY_APP_ID`
- `PEP_PROXY_USERNAME`
- `PEP_PASSWORD`

Your endpoint being exposed, for example if you reverse proxy this for the
MYORG organization with https://jcci.yourdomain.tld/ you have to set the
following:

- `SPARTA_EXPOSED_HOST: jcci.yourdomain.tld`
- `SPARTA_EXPOSED_PORT: 443`
- `SPARTA_ORG: MYORG`


As for the upstream system you'll have to set your organization data through
container volumes mounted in `/app/data` and `/app/data/learning` folders with
the appropriate JSON file.

The `wadl_capabilities.xml` resource endpoint and name is updated on the fly,
no need to edit it (see the exposed host, port and org above)


You can also check `role-sparta-jcci-docker/` for an example deployment
