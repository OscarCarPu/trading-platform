# Plan 

## Phase 1

### Functional requirements 

- Download historical marke data from sources 
- Run scheduled loads 
- Backfill historical ranges 
- Store raw data 
- Clean, normalize, validate data and pass to process data storing 
- Exploratory basic queries
- Idempotent reruns 
- Logs, monitoring and alert systems, don't fail silently

### Checks 

- [ ] Investigate and decide data sources 
- [ ] Mount architecture basic 
- [ ] First orchestration spark raw data
- [ ] Orchestration pipelines processing data 
- [ ] First exploratory basic queries 
- [ ] More sources or more data in, go to large data quantities 
- [ ] Reviewing and cycling back till good phase 1
