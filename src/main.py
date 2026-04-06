def validate_config(config):
    """
    Validates the cloud plan against core AWS architecture concepts.
    """
    resources = config.get("resources", [])
    
    # Check for VPC (Essential for Cloud Planning & Strategy)
    has_vpc = any(res.get('type') == 'VPC' for res in resources)
    
    # Check for Subnets (Essential for Web Service Architecture)
    has_subnets = any(res.get('type') == 'Subnet' for res in resources)
    
    # Validation logic for Syllabus Coverage
    if not has_vpc:
        print("Validation Error: No VPC defined in the infrastructure plan.")
        return False
    if not has_subnets:
        print("Validation Error: Infrastructure requires at least one Subnet.")
        return False
        
    return True
