# Windows Firewall Configuration Script

# Enable script execution
Set-ExecutionPolicy RemoteSigned -Scope Process

# Function to create firewall rules
function Create-FirewallRules {
    Write-Host "Creating firewall rules..."
    
    # Block Telnet (Port 23)
    New-NetFirewallRule -DisplayName "Block Telnet" -Direction Inbound -Protocol TCP -LocalPort 23 -Action Block
    
    # Block SSH (Port 22)
    New-NetFirewallRule -DisplayName "Block SSH" -Direction Inbound -Protocol TCP -LocalPort 22 -Action Block
    
    # Allow RDP (Port 3389)
    New-NetFirewallRule -DisplayName "Allow RDP" -Direction Inbound -Protocol TCP -LocalPort 3389 -Action Allow
    
    # Block ICMP (Ping)
    New-NetFirewallRule -DisplayName "Block ICMP" -Direction Inbound -Protocol ICMPv4 -Action Block
    
    Write-Host "Rules created successfully!"
}

# Main script execution
Create-FirewallRules
