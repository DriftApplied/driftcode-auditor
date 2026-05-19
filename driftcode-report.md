# DriftCode Auditor Report

**Target:** /home/kilo/simgame

**Total issues:** 105

## Maintainability
- **long_line** in `/home/kilo/simgame/lib/slickipedia-template.ts:8`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/commandHelp.ts:4`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/commandHelp.ts:9`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/filesystem.ts:112`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/filesystem.ts:113`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/filesystem.ts:298`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/filesystem.ts:400`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/filesystem.ts:443`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/filesystem.ts:483`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/filesystem.ts:504`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/filesystem.ts:505`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/filesystem.ts:577`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/filesystem.ts:591`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/filesystem.ts:618`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/apt.ts:168`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/apt.ts:181`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/apt.ts:210`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/apt.ts:257`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/apt.ts:266`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/apt.ts:269`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/apt.ts:300`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/apt.ts:338`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/apt.ts:348`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:22`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:26`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:34`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:38`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:50`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:85`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:86`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:90`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:92`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:93`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:94`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:113`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/reboot.ts:114`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/nmap.ts:186`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/nmap.ts:206`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/nmap.ts:214`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/nmap.ts:272`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/nmap.ts:278`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/nmap.ts:279`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/nmap.ts:286`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/internet.ts:117`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/internet.ts:286`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/internet.ts:556`: Line >100 chars

- **long_line** in `/home/kilo/simgame/lib/internet.ts:616`: Line >100 chars

## Privacy
- **pii** in `/home/kilo/simgame/lib/commandHelp.ts:57`: PII in code → `commands.push(['geemail', 'GeeMail email client']);`

- **pii** in `/home/kilo/simgame/lib/filesystem.ts:443`: PII in code → `'  Available packages: nano (text editor), browser (web browser), nmap (network scanner), snake (game), geemail (email client)\n' +`

- **pii** in `/home/kilo/simgame/lib/apt.ts:55`: PII in code → `description: 'GeeMail email client for sending and receiving virtual emails',`

- **pii** in `/home/kilo/simgame/lib/apt.ts:59`: PII in code → `provides: ['email-client']`

- **pii** in `/home/kilo/simgame/lib/internet.ts:21`: PII in code → `email: string;`

- **pii** in `/home/kilo/simgame/lib/internet.ts:33`: PII in code → `export interface Email {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:79`: PII in code → `emails: Email[];`

- **pii** in `/home/kilo/simgame/lib/internet.ts:126`: PII in code → `parsed.emails = (parsed.emails || []).map((email: any) => ({`

- **pii** in `/home/kilo/simgame/lib/internet.ts:127`: PII in code → `...email,`

- **pii** in `/home/kilo/simgame/lib/internet.ts:128`: PII in code → `starred: email.starred ?? false,`

- **pii** in `/home/kilo/simgame/lib/internet.ts:129`: PII in code → `labels: email.labels ?? ['inbox'],`

- **pii** in `/home/kilo/simgame/lib/internet.ts:130`: PII in code → `threadId: email.threadId ?? email.id,`

- **pii** in `/home/kilo/simgame/lib/internet.ts:131`: PII in code → `cc: email.cc ?? [],`

- **pii** in `/home/kilo/simgame/lib/internet.ts:132`: PII in code → `bcc: email.bcc ?? [],`

- **pii** in `/home/kilo/simgame/lib/internet.ts:133`: PII in code → `attachments: email.attachments ?? []`

- **pii** in `/home/kilo/simgame/lib/internet.ts:438`: PII in code → `// Email methods`

- **pii** in `/home/kilo/simgame/lib/internet.ts:439`: PII in code → `getEmails(): Email[] {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:443`: PII in code → `addEmail(email: Email): void {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:444`: PII in code → `this.data.emails.push(email);`

- **pii** in `/home/kilo/simgame/lib/internet.ts:454`: PII in code → `if (this.data.emailAccounts.some(acc => acc.email === account.email)) {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:462`: PII in code → `getEmailAccount(email: string): EmailAccount | null {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:463`: PII in code → `return this.data.emailAccounts.find(acc => acc.email === email) || null;`

- **pii** in `/home/kilo/simgame/lib/internet.ts:466`: PII in code → `authenticateEmailAccount(email: string, password: string): boolean {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:467`: PII in code → `const account = this.getEmailAccount(email);`

- **pii** in `/home/kilo/simgame/lib/internet.ts:481`: PII in code → `email: playerEmail,`

- **pii** in `/home/kilo/simgame/lib/internet.ts:494`: PII in code → `// Enhanced email management methods`

- **pii** in `/home/kilo/simgame/lib/internet.ts:496`: PII in code → `const email = this.data.emails.find(e => e.id === emailId);`

- **pii** in `/home/kilo/simgame/lib/internet.ts:497`: PII in code → `if (email) {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:498`: PII in code → `email.read = read;`

- **pii** in `/home/kilo/simgame/lib/internet.ts:504`: PII in code → `const email = this.data.emails.find(e => e.id === emailId);`

- **pii** in `/home/kilo/simgame/lib/internet.ts:505`: PII in code → `if (email) {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:506`: PII in code → `email.starred = starred;`

- **pii** in `/home/kilo/simgame/lib/internet.ts:512`: PII in code → `const email = this.data.emails.find(e => e.id === emailId);`

- **pii** in `/home/kilo/simgame/lib/internet.ts:513`: PII in code → `if (email && !email.labels.includes(label)) {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:514`: PII in code → `email.labels.push(label);`

- **pii** in `/home/kilo/simgame/lib/internet.ts:520`: PII in code → `const email = this.data.emails.find(e => e.id === emailId);`

- **pii** in `/home/kilo/simgame/lib/internet.ts:521`: PII in code → `if (email) {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:522`: PII in code → `email.labels = email.labels.filter(l => l !== label);`

- **pii** in `/home/kilo/simgame/lib/internet.ts:542`: PII in code → `getEmailsByLabel(label: string): Email[] {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:543`: PII in code → `return this.data.emails.filter(email => email.labels.includes(label));`

- **pii** in `/home/kilo/simgame/lib/internet.ts:546`: PII in code → `getThreadEmails(threadId: string): Email[] {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:547`: PII in code → `return this.data.emails.filter(email => email.threadId === threadId)`

- **pii** in `/home/kilo/simgame/lib/internet.ts:551`: PII in code → `createReplyEmail(originalEmail: Email, replyBody: string, playerEmail: string): Email {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:552`: PII in code → `const replyEmail: Email = {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:568`: PII in code → `searchEmails(query: string, currentUserEmail?: string): Email[] {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:570`: PII in code → `return this.data.emails.filter(email => {`

- **pii** in `/home/kilo/simgame/lib/internet.ts:574`: PII in code → `email.from === currentUserEmail ||`

- **pii** in `/home/kilo/simgame/lib/internet.ts:575`: PII in code → `email.to === currentUserEmail ||`

- **pii** in `/home/kilo/simgame/lib/internet.ts:576`: PII in code → `(email.cc && email.cc.includes(currentUserEmail)) ||`

- **pii** in `/home/kilo/simgame/lib/internet.ts:577`: PII in code → `(email.bcc && email.bcc.includes(currentUserEmail));`

- **pii** in `/home/kilo/simgame/lib/internet.ts:581`: PII in code → `return email.from.toLowerCase().includes(lowerQuery) ||`

- **pii** in `/home/kilo/simgame/lib/internet.ts:582`: PII in code → `email.to.toLowerCase().includes(lowerQuery) ||`

- **pii** in `/home/kilo/simgame/lib/internet.ts:583`: PII in code → `email.subject.toLowerCase().includes(lowerQuery) ||`

- **pii** in `/home/kilo/simgame/lib/internet.ts:584`: PII in code → `email.body.toLowerCase().includes(lowerQuery);`

## Architecture
- **large_file** in `/home/kilo/simgame/lib/commandHelp.ts:1`: File >500 lines

- **large_file** in `/home/kilo/simgame/lib/filesystem.ts:1`: File >500 lines

- **large_file** in `/home/kilo/simgame/lib/manPages.ts:1`: File >500 lines

- **large_file** in `/home/kilo/simgame/lib/internet.ts:1`: File >500 lines

## Summary
Clean code recommended. Run with --privacy or --maintainability for focus.
