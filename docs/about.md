# About

This page is dedicated to information about the H&H Local AI Project and the company.

---

## Project Overview

The H&H Local AI Project is a collaboration between the H&H Molds team and the [H&H Molds Inc.](https://hhmoldsinc.com/) company.

- Purpose: Provide a local, secure AI assistant for H&H Molds to support injection molding operations, data analysis, and internal knowledge retrieval.
- Maintainers: Dawson B.

### Project Goals
- Provide a local, secure AI assistant for H&H Molds to support injection molding operations, data analysis, and internal knowledge retrieval.

## Code Layout

### Github Repository
https://github.com/pegasora/local-ai

**Note**: This is private github repository, so you will need to be a member of the HH Molds Inc. Currently, only Gary and Dawson have access to the repository.

### Docs
https://github.com/pegasora/HHDocs

- This is where you will find the documentation for the project, may be out-of-date at a later point. 
- To see the most up-to-date docs, you will need to build them via docsify from the Local-AI repository (the /docs folder).
- Gary will be in charge of maintaining this documentation and any new additions.

--- 

## Ubuntu Workstation Layout 

### Tank 
/tank is the mount point for the 4TB HDD drive where all of the data for images, chromadb, and others currently lives. Supabase's data is in the /home/local-ai folder as of right now, 
and in the future will be moved to the tank. This is very long term, does not need to happen right now. It is in the root area of the system, and therefore will need sudo (admin) access.

### Local AI 

### Pydantic-models 
Everything related to the Pydantic models is located in the /home/local-ai/pydantic-models folder. The pydantic folder has the following layout:

- /pydantic-models/models
- /pydantic-models/tests
- /pydantic-models/scripts
- /pydantic-models/README.md

The models folder contains all of the pydantic models for the project.

---

## Company Overview
H&H Molds is a full service mold-making and injection molding company providing 
total plastics services to a growing list of industries, including electronics, 
telecommunications, medical, pharmaceutical, sports, utilities, agricultural, 
food and dairy.

H&H Molds Inc. is committed to advancing the injection molding opportunities for smaller 
companies looking to break into the market. Their innovation and adaption to new technologies
is what birthed this summer internship, and helps bring reliable production to their customers. 

The company is a leader in the industry, with a strong reputation for quality and reliability. 
They have a long history of providing high-quality products and services to their customers, 
and their commitment to excellence is evident in their innovative approach to product development 
and their dedication to customer satisfaction.

---

## About Dawson B.


## Contact
If you have any questions or feedback, please reach out to the project maintainers:

- Dawson B. — intern@hhmoldsinc.com **or** dawsonhburgess@gmail.com
- Paul R. — quality@hhmoldsinc.com
- Gary B. — garyb@hhmoldsinc.com
