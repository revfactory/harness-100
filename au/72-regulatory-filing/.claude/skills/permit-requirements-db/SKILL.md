---
name: permit-requirements-db
description: "A requirements database that systematically organises permit and license requirements and required documents by industry. The 'requirements-investigator' and 'submission-verifier' agents must use this skill's requirements DB and checklist rules when investigating permit requirements and verifying document completeness. Use for 'permit requirement lookup', 'required documents check', 'license condition review', etc. Note: drafting applications or preparing attachments is outside the scope of this skill."
---

# Permit Requirements DB — Industry-Specific Permit & License Requirements Database

A DB that systematically organises permit/license types, requirements, required documents, and processing times for major industries.

## Permit/License Type Classification

### Permit · Authorisation · Registration · Notification Distinction

| Type | Legal Nature | Review Intensity | Examples |
|------|-------------|-----------------|---------|
| Permit | Prohibition lifted (discretionary) | High | Restaurant business permit, building permit |
| Authorisation | Supplementary act (binding) | High | Corporate establishment authorisation, merger authorisation |
| Registration | Accepted upon meeting requirements | Medium | Mail-order business, tutoring centre registration |
| Notification | Effective upon receipt (self-completing) | Low | Business registration, home-sharing notification |
| License | Qualification-based permit | High | Medical institution establishment, pharmacy |

## Permit/License Requirements by Major Industry

### Restaurant (General Restaurant Business Permit)

```
Jurisdiction: City/County/District Health and Sanitation Department
Legal basis: Food Sanitation Act Article 37
Processing time: 10 days

Personal requirements:
  - No disqualifying grounds under the Food Sanitation Act
  - Completion of sanitation education (6 hours, in advance)
  
Physical requirements:
  - Kitchen: Facilities in direct contact with food (stainless steel)
  - Water supply: Municipal water or water meeting drinking water quality standards
  - Restroom: Separated from kitchen
  - Ventilation: Exhaust system for smoke and steam generated during cooking

Required documents:
  1. Business permit application form (designated form)
  2. Floor plan of business facility (by floor)
  3. Education completion certificate (sanitation education)
  4. Water quality inspection report (if using groundwater)
  5. Building register (for use confirmation)
  6. Representative's ID
  Fee: KRW 28,000
```

### Mail-Order Business (Registration)

```
Jurisdiction: City/County/District Office
Legal basis: E-Commerce Act Article 12
Processing time: Immediate ~ 3 days

Requirements:
  - Completed business registration
  - Purchase safety service enrollment (escrow or consumer damage compensation insurance)

Required documents:
  1. Mail-order business notification form
  2. Copy of business registration certificate
  3. Purchase safety service enrollment confirmation
  Fee: None
```

### Cosmetics Manufacturing Business (Registration)

```
Jurisdiction: Regional Food and Drug Administration
Legal basis: Cosmetics Act Article 3
Processing time: 14 days

Personal requirements:
  - Qualification or experience related to cosmetics manufacturing
  - Quality control manager (science/engineering bachelor's degree or higher)

Physical requirements:
  - Manufacturing facilities: Production room, storage room, testing room
  - Quality control: Test and inspection equipment
  - CGMP standards compliance (recommended)

Required documents:
  1. Cosmetics manufacturing business registration application
  2. Facility specification sheet + floor plan
  3. Quality control manager qualification documents
  4. Copy of business registration certificate
```

### Software Business Operator (Notification)

```
Jurisdiction: Korea Software Industry Association
Legal basis: Software Industry Promotion Act Article 24
Processing time: 7 days

Requirements:
  - Completed business registration
  - Intent to conduct SW-related business

Required documents:
  1. SW business operator notification form
  2. Copy of business registration certificate
  3. Business premises lease agreement (if required)
```

## Document Issuance Location & Processing Time Guide

| Document | Issuance Location | Processing Time | Validity Period | Fee |
|----------|------------------|----------------|----------------|-----|
| Business registration certificate | Tax office / Hometax | Immediate ~ 3 days | Indefinite | Free |
| Building register | Government24 | Immediate | 3 months | Free |
| Registry certificate | Internet Registry | Immediate | 3 months | KRW 1,000 |
| Sanitation education certificate | Food Sanitation Education Institute | 1 day | 3 years | Education fee |
| Water quality inspection report | Inspection agency | 7–14 days | 3 years | KRW 100,000+ |
| Fire facility completion certificate | Fire station | 7 days | 1 year | Free |
| Background check | Police station | 3 days | 6 months | Free |

## Permit/License Completeness Checklist

```
□ Step 1: Confirm permit/license type
  - [ ] Does it fall under permit / registration / notification?
  - [ ] Confirm jurisdiction

□ Step 2: Review personal requirements
  - [ ] Check for disqualifying grounds
  - [ ] Required qualifications/experience met
  - [ ] Prior education completed

□ Step 3: Review physical requirements
  - [ ] Facility standards met
  - [ ] Equipment and fixtures in place
  - [ ] Floor area requirements met

□ Step 4: Document completeness
  - [ ] All required documents obtained
  - [ ] Documents within validity period
  - [ ] Accuracy of entered information

□ Step 5: Final check before submission
  - [ ] Fee prepared
  - [ ] Submission date/time confirmed
  - [ ] Prepared for possible corrections
```

## References

- Government24, individual local government civil affairs guidance standards
- Detailed industry-specific requirements: see `references/permit-details.md`
