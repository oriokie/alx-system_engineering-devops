<img src=./image.png width=50%>

## Issue Summary:

Duration: May 8th 2024, 10 AM  - May 9th 2024 12 PM

Impact: Our web application experienced a significant outage, affecting all users worldwide. Users reported inability to access the service, resulting in a 100% outage.

Root Cause: The outage was caused by a misconfiguration in the load balancer that lead to an overload in the backend servers, and subsequent service degradation.


## Timeline:

May 8th, 2024, 10:00 AM (UTC): Issue detected by automated monitoring system triggering alerts for high server load.

May 8th, 2024, 10:10 AM (UTC): Engineers noticed a spike in error rates and user complaints regarding slow performance.

Actions Taken: Investigated backend servers for performance issues; assumed high traffic was the root cause.

Escalation: Incident escalated to the infrastructure team and senior developers for further investigation and resolution.

Resolution: Load balancer misconfiguration identified as the root cause and corrected; traffic distribution normalized, restoring service.



## Root cause and resolution:

Root Cause Explanation: The load balancer misconfiguration caused it to send an excessive number of requests to a subset of backend servers, overwhelming them and degrading overall performance.

Resolution Details: The load balancer configuration was adjusted to evenly distribute traffic among all available backend servers. Additionally, monitoring alerts were refined to detect similar issues promptly.


## Coirrective and Preventative Measures:

Implement automated testing for load balancer configurations to catch misconfigurations before deployment.

Conduct regular audits of system configurations to ensure alignment with best practices.

Enhance monitoring systems to provide more granular insights into server performance and traffic patterns.

By addressing these corrective and preventative measures, we aim to minimize the risk of similar outages in the future and ensure the continued reliability and availability of our services
