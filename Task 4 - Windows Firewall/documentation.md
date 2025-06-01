# Windows Firewall Configuration Documentation

## Configuration Details

### Firewall Rules Created:
1. Block Telnet (Port 23)
   - Direction: Inbound
   - Protocol: TCP
   - Action: Block

2. Block SSH (Port 22)
   - Direction: Inbound
   - Protocol: TCP
   - Action: Block

3. Allow RDP (Port 3389)
   - Direction: Inbound
   - Protocol: TCP
   - Action: Allow

4. Block ICMP (Ping)
   - Direction: Inbound
   - Protocol: ICMPv4
   - Action: Block

## Testing Results

### Telnet (Port 23)
- Should be blocked
- Expected result: Connection failure

### SSH (Port 22)
- Should be blocked
- Expected result: Connection failure

### RDP (Port 3389)
- Should be allowed
- Expected result: Connection success

### ICMP (Ping)
- Should be blocked
- Expected result: No response

## Security Notes
- All rules are configured for inbound traffic only
- Rules are applied to all network profiles (Domain, Private, Public)
- Administrative privileges required for rule creation
- Rules can be removed using the cleanup script

## Usage Instructions
1. Run firewall_rules.ps1 to create rules
2. Run firewall_tests.ps1 to verify rules
3. Run firewall_cleanup.ps1 to remove rules

## Required Permissions
- Administrative privileges required for:
  - Creating firewall rules
  - Testing connections
  - Removing rules
