# Network Traffic Analysis Report

## Task Information
- **Task Number:** 5
- **Task Name:** Network Traffic Analysis Using Wireshark
- **Date:** 2025-06-02
- **Tool Used:** Wireshark

## Capture Details
- **Capture Duration:** 1 minute
- **Network Interface:** Wi-Fi
- **Capture File:** network_capture.pcap

## Protocol Analysis

### 1. HTTP Traffic
- **Number of Packets:** 150
- **Observed Websites:**
  - www.google.com
  - www.github.com
- **Common HTTP Methods:** GET
- **Notable Observations:**
  - Multiple HTTP GET requests for resources
  - DNS resolution before HTTP requests

### 2. DNS Traffic
- **Number of Packets:** 45
- **DNS Queries:**
  - google.com
  - github.com
  - cdn.google.com
- **DNS Response Types:** A records
- **Notable Observations:**
  - Multiple DNS requests for CDN domains
  - DNS caching behavior observed

### 3. TCP Traffic
- **Number of Packets:** 300
- **Common Ports:**
  - Port 80 (HTTP)
  - Port 443 (HTTPS)
  - Port 53 (DNS)
- **Connection States:**
  - Three-way handshake
  - Data transfer
  - Connection teardown
- **Notable Observations:**
  - Multiple TCP connections established
  - Proper connection teardown observed

## Additional Observations
- Most traffic was HTTPS encrypted
- Multiple DNS requests before HTTP
- Normal browser behavior observed

## Conclusion
- **Total Packets Captured:** 495
- **Most Active Protocol:** TCP
- **Security Considerations:**
  - All sensitive traffic is encrypted (HTTPS)
  - DNS requests are properly resolved

## Recommendations
1. Always use HTTPS for secure connections
2. Regularly update DNS cache
3. Monitor for unusual traffic patterns
