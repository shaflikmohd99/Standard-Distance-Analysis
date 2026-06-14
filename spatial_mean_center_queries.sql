-- ==============================================================================
-- Script Name: 01_spatial_filter_mean_center.sql
-- Description: Filters the enterprise database to create a clean, valid view of 
--              sustainability initiatives for Mean Center (center of gravity) tracking.
-- ==============================================================================

CREATE OR REPLACE VIEW sustainability_initiatives_mc AS
SELECT 
    objectid,
    project_id,
    project_category,
    total_budget,
    shape -- The native enterprise geometry column (e.g., ST_Geometry)
FROM 
    enterprise_sde.sustainability_projects_raw
WHERE 
    -- 1. Attribute Filter: Only track active or officially planned projects
    status IN ('Active', 'Planned')
    
    -- 2. Spatial Cleanliness: Null geometries will crash the Mean Center tool
    AND shape IS NOT NULL
    AND ST_IsValid(shape) = 1
    AND ST_IsEmpty(shape) = 0;

-- Optional: Verify the clean record count before moving to Python processing
SELECT COUNT(*) as valid_projects FROM sustainability_initiatives_mc;
