Name: ARSHIA JAIN SRN: PES2UG23CS095

Which issues were the easiest to fix, and which were the hardest? Why?
Answer: Naming conventions were the easiest to fix, these were simple styling fixes - changing function names to snake_cases. the hardest to fix was the global variable usage and use of eval(), these need structure editing, not just syntax edits. removing the global variable or minimizing its usage meant to change the code carefully, as the stock data is central to the system, it was tricky to preserve behavior while keeping the code modular and testable.

Did the static analysis tools report any false positives? If so, describe one example.
Answer: yes, global statement. the code used global stock_Data, in a controlled context for updating a shared state dictionary. while global is discouraged in large system, in this small self-contained script its not a real bug, it just not ideal for scalability

How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
Answer: 1.during local development - installing extensions in VSCode/Codespaces - gives us immediate feedback while coding, like underlines the issues in real time 2.Continuos integration - configure in github actions/gitlab CL - automatically runs pylint, bandit, and flask8 for every pull request 3.periodic audits - schedule bandit scans weekly or before releases - ensures no security regressions creeps in over time

What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
Answer: more readable, easier to maintain(defaults are safely handled), more Secure(removal of eval()) , and file safety(opening and closing)