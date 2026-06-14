-- ==============================================================================
-- Script Name: 01_spatial_filter_sustainability.sql
-- Description: Filters the enterprise database to create a clean view of active 
--              sustainability initiatives for spatial statistics modeling.
-- ==============================================================================

CREATE OR REPLACE VIEW sustainability_initiatives AS
SELECT 
    objectid,
    project_id,
    project_type,   -- e.g., 'Solar', 'Green Roof', 'Rainwater Harvesting'
    budget,
    shape           -- Native geometry column
FROM 
    enterprise_sde.sustainability_projects_raw
WHERE 
    -- 1. Attribute Filter: Only include completed or active projects
    status IN ('Active', 'Completed')
    
    -- 2. Spatial Cleanliness: Exclude records with missing or corrupt coordinates
    --    (A null geometry will crash the Standard Distance tool)
    AND shape IS NOT NULL
    AND ST_IsEmpty(shape) = 0
    AND ST_IsValid(shape) = 1;

-- Optional: Check the distribution of project types before running Python
SELECT project_type, COUNT(*) as project_count 
FROM sustainability_initiatives 
GROUP BY project_type;
