-- ==============================================================================
-- Script Name: 01_spatial_filter_ellipse.sql
-- Description: Queries the Enterprise SDE database to isolate valid spatial 
--              features for Directional Distribution (Ellipse) tracking.
-- ==============================================================================

-- Create a spatial view that ArcPy will call as the source layer
CREATE OR REPLACE VIEW sustainability_initiatives_sde AS
SELECT 
    objectid,
    project_id,
    project_name,
    funding_year,
    shape -- The native enterprise geometry column (e.g., ST_Geometry)
FROM 
    enterprise_sde.sustainability_projects_raw
WHERE 
    -- 1. Temporal Filter: Isolate active projects from recent cycles
    funding_year >= 2020
    
    -- 2. Geometry Validation: Ensure no null or empty shapes skew the trend calculation
    AND shape IS NOT NULL
    AND ST_IsValid(shape) = 1
    AND ST_IsEmpty(shape) = 0;

-- Optional: Quick diagnostic to ensure an adequate sample size for directional analysis
SELECT COUNT(*) as total_analytical_points FROM sustainability_initiatives_sde;
