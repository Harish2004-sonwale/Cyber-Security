# Firewall Testing Script

# Function to test firewall rules
function Test-FirewallRules {
    Write-Host "Testing firewall rules..."
    
    # Test Telnet connection
    Write-Host "Testing Telnet (Port 23):"
    Test-NetConnection -ComputerName localhost -Port 23
    
    # Test SSH connection
    Write-Host "Testing SSH (Port 22):"
    Test-NetConnection -ComputerName localhost -Port 22
    
    # Test RDP connection
    Write-Host "Testing RDP (Port 3389):"
    Test-NetConnection -ComputerName localhost -Port 3389
    
    # Test ICMP (Ping)
    Write-Host "Testing ICMP (Ping):"
    Test-Connection -ComputerName localhost -Count 1
}

# Main script execution
Test-FirewallRules
