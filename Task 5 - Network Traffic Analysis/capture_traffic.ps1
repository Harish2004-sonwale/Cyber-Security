# Network Traffic Capture Script
# This script uses PowerShell to capture network traffic

# Function to capture network traffic
function Capture-NetworkTraffic {
    param(
        [Parameter(Mandatory=$true)]
        [string]$OutputFile
    )

    Write-Host "Starting network traffic capture..."
    
    # Use PowerShell's built-in networking capabilities to capture traffic
    # Note: This is a simplified version for demonstration purposes
    # In practice, Wireshark should be used for actual packet capture
    
    # Create a log file
    $logFile = Join-Path $OutputFile "network_capture.txt"
    
    # Capture basic network information
    $networkInfo = @{
        "Date" = (Get-Date).ToString()
        "Hostname" = $env:COMPUTERNAME
        "IPAddresses" = (Get-NetIPAddress | Where-Object {$_.AddressFamily -eq 'IPv4'}).IPAddress
        "NetworkInterfaces" = (Get-NetAdapter | Select-Object Name, Status, MacAddress)
    }

    # Save to file
    $networkInfo | ConvertTo-Json | Out-File $logFile
    
    Write-Host "Network capture completed. Results saved to $logFile"
}

# Main script execution
$captureDir = Join-Path $PSScriptRoot "capture"
if (-not (Test-Path $captureDir)) {
    New-Item -ItemType Directory -Path $captureDir -Force
}

$timestamp = (Get-Date -Format "yyyyMMdd_HHmmss")
$outputFile = Join-Path $captureDir "network_capture_$timestamp"

Capture-NetworkTraffic -OutputFile $outputFile
