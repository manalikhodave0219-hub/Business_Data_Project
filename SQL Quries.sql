
DROP TABLE IF EXISTS business_data;

CREATE TABLE business_data (
    business_id TEXT,
    business_name TEXT,
    city TEXT,
    industry TEXT,
    business_type TEXT,
    contact_number TEXT,
    address TEXT,
    services TEXT,
    online_presence TEXT,
    google_rating TEXT,
    website TEXT,
    problem_category TEXT,
    manual_process TEXT,
    pain_point TEXT,
    required_service TEXT,
    requirement_type TEXT,
    evidence_type TEXT,
    requirement_status TEXT,
    urgency TEXT,
    budget_status TEXT,
    follow_up_status TEXT,
    collection_date TEXT,
    source_url TEXT
);

SELECT * FROM business_data;

SELECT COUNT(*) AS total_businesses
FROM business_data;

SELECT business_id, COUNT(*) AS count
FROM business_data
GROUP BY business_id
HAVING COUNT(*) > 1;

SELECT *
FROM business_data
WHERE business_id IS NULL;

DELETE FROM business_data
WHERE business_id IS NULL;

SELECT city, COUNT(*) AS total_businesses
FROM business_data
GROUP BY city
ORDER BY total_businesses DESC;

SELECT industry, COUNT(*) AS total_businesses
FROM business_data
GROUP BY industry
ORDER BY total_businesses DESC;

SELECT problem_category, COUNT(*) AS total_businesses
FROM business_data
GROUP BY problem_category
ORDER BY total_businesses DESC;

SELECT online_presence, COUNT(*) AS total_businesses
FROM business_data
GROUP BY online_presence
ORDER BY total_businesses DESC;

SELECT
    CASE
        WHEN website IS NULL
             OR TRIM(website) = ''
             OR LOWER(TRIM(website)) IN ('not found', 'no website found', 'not available')
        THEN 'No Website'
        ELSE 'Website Available'
    END AS website_status,
    COUNT(*) AS total_businesses
FROM business_data
GROUP BY website_status
ORDER BY total_businesses DESC;

SELECT requirement_status, COUNT(*) AS total_businesses
FROM business_data
GROUP BY requirement_status
ORDER BY total_businesses DESC;

SELECT evidence_type, COUNT(*) AS total_businesses
FROM business_data
GROUP BY evidence_type
ORDER BY total_businesses DESC;

SELECT requirement_type, COUNT(*) AS total_businesses
FROM business_data
GROUP BY requirement_type
ORDER BY total_businesses DESC;

SELECT urgency, COUNT(*) AS total_businesses
FROM business_data
GROUP BY urgency
ORDER BY total_businesses DESC;

SELECT budget_status, COUNT(*) AS total_businesses
FROM business_data
GROUP BY budget_status
ORDER BY total_businesses DESC;

SELECT follow_up_status, COUNT(*) AS total_businesses
FROM business_data
GROUP BY follow_up_status
ORDER BY total_businesses DESC;

SELECT
    city,
    COUNT(*) AS total_businesses,
    SUM(
        CASE
            WHEN website IS NULL
                 OR TRIM(website) = ''
                 OR LOWER(TRIM(website)) IN
                    ('not found', 'no website found', 'not available')
            THEN 1
            ELSE 0
        END
    ) AS no_website
FROM business_data
GROUP BY city
ORDER BY no_website DESC;

SELECT
    industry,
    COUNT(*) AS total_businesses,
    SUM(
        CASE
            WHEN website IS NULL
                 OR TRIM(website) = ''
                 OR LOWER(TRIM(website)) IN
                    ('not found', 'no website found', 'not available')
            THEN 1
            ELSE 0
        END
    ) AS no_website
FROM business_data
GROUP BY industry
ORDER BY no_website DESC;

SELECT
    requirement_status,
    COUNT(*) AS total_businesses
FROM business_data
WHERE website IS NULL
   OR TRIM(website) = ''
   OR LOWER(TRIM(website)) IN
      ('not found', 'no website found', 'not available')
GROUP BY requirement_status
ORDER BY total_businesses DESC;

SELECT
    city,
    industry,
    COUNT(*) AS total_businesses
FROM business_data
GROUP BY city, industry
ORDER BY city, total_businesses DESC;

SELECT
    business_name,
    city,
    industry,
    problem_category,
    required_service,
    requirement_type,
    requirement_status,
    urgency
FROM business_data
WHERE requirement_status IN
      ('Potential Need', 'Requirement Identified', 'Active Opportunity')
ORDER BY
    CASE urgency
        WHEN 'High' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'Low' THEN 3
        ELSE 4
    END;

	SELECT
    industry,
    COUNT(*) AS no_website_businesses
FROM business_data
WHERE website IS NULL
   OR TRIM(website) = ''
   OR LOWER(TRIM(website)) IN
      ('not found', 'no website found', 'not available')
GROUP BY industry
ORDER BY no_website_businesses DESC;

	SELECT COUNT(*) AS no_website_businesses
FROM business_data
WHERE website IS NULL
   OR TRIM(website) = ''
   OR LOWER(TRIM(website)) IN
      ('not found', 'no website found', 'not available');

	  SELECT
    city,
    COUNT(*) AS no_website_businesses
FROM business_data
WHERE website IS NULL
   OR TRIM(website) = ''
   OR LOWER(TRIM(website)) IN
      ('not found', 'no website found', 'not available')
GROUP BY city
ORDER BY no_website_businesses DESC;
