# Password Analysis Script

# Function to run Python script and analyze results
function Run-PasswordAnalysis {
    Write-Host "Running password analysis..."
    
    # Run Python script
    python password_generator.py
    
    # Check if analysis file exists
    if (Test-Path "password_analysis.json") {
        Write-Host "Password analysis completed. Results saved to password_analysis.json"
        
        # Display analysis results
        $results = Get-Content -Raw "password_analysis.json" | ConvertFrom-Json
        foreach ($password in $results.PSObject.Properties) {
            Write-Host "`nPassword Type: $($password.Name)"
            Write-Host "Password: $($password.Value.password)"
            Write-Host "Metrics:"
            $password.Value.metrics | Format-List
        }
    }
    else {
        Write-Host "Error: Password analysis failed. JSON file not found."
    }
}

# Main script execution
Run-PasswordAnalysis
