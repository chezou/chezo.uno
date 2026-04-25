---
title: TikTok kept letting strangers create accounts with my email, so I filed PIPEDA
  and CASL complaints
subtitle: ''
summary: ''
date: 2026-04-24 18:53:00-07:00
lastmod: ''
categories: []
tags: [privacy, Canada]
draft: false
featured: false
image: null
recommendations: [/blog/2019-11-26_how-to-release-python-package-from-github-actions-d5a1d8edba6e/,
  /blog/2020-03-05_py-operator-development-guide-for-python-users/, /blog/2022-05-21_fastest-way-to-release-python-cli/]
---

> [!CAUTION]+ Disclaimer 
> This is a personal account of how I, a non-lawyer Canadian resident, used PIPEDA and CASL to address a privacy issue with TikTok. **It is not legal advice.** Procedures, deadlines, and applicable laws change. If you are facing a similar situation, please verify everything against current OPC and CRTC guidance, and consider consulting a lawyer for matters with significant legal or financial stakes. Parts of the research and drafting in this article were done with the help of an LLM. I reviewed the output, but factual errors are still possible. Please check the primary sources I link to before acting on anything here.

## TL;DR

- TikTok accounts I never created kept showing up under my email address. The first one was `@chezou2`. After it was deleted, a different handle appeared.
- TikTok lets people register accounts without verifying that they control the email address. This is a structural failure to obtain consent.
- TikTok Support eventually deleted the first account after I escalated. A different account appeared shortly after the deadline I had given them.
- I filed two complaints with Canadian regulators:
    - A [**CASL**](https://laws-lois.justice.gc.ca/eng/acts/E-1.6/) **violation report** to the [**CRTC Spam Reporting Centre**](https://www.fightspam.gc.ca/) 
    - A [**PIPEDA**](https://laws-lois.justice.gc.ca/eng/acts/p-8.6/) **formal complaint** to the [**Office of the Privacy Commissioner of Canada (OPC)**](https://www.priv.gc.ca/) 
- The OPC had already issued a joint Report of Findings against TikTok in September 2025 ([#2025-003](https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2025/pipeda-2025-003/)), so my complaint joins an existing thread of regulatory attention.
- Below is what I did. Whether anything from this is useful for your own situation is for you to judge.

-----

## What is PIPEDA and CASL?

If you live in Canada and you have never come across these acronyms, here is the short version.

**PIPEDA** stands for the Personal Information Protection and Electronic Documents Act. It is the federal law that governs how private-sector organizations collect, use, and disclose personal information in the course of commercial activity. Your email address is personal information under PIPEDA. Complaints about PIPEDA go to the **OPC**, the Office of the Privacy Commissioner of Canada.

**CASL** stands for Canada's Anti-Spam Legislation. It regulates the sending of "commercial electronic messages" (think marketing emails) without consent. Complaints about CASL go to the **CRTC** through its Spam Reporting Centre.

The two laws cover different things. PIPEDA is about what an organization does with your personal information. CASL is about whether an organization is allowed to send you a particular email. In my case, both were relevant for different reasons.

## What happened

In November 2025, I started receiving emails from `noreply@account.tiktok.com` reporting "a new device login." The login was from an Android phone I do not own. More fundamentally, I have never created a TikTok account.

The emails were addressed to my private email and referenced a handle, `@chezou2`, that someone had registered with a name close to mine. There was an awkward fact behind this: **TikTok lets people register accounts without verifying that the email address belongs to them.** No "is this you?" confirmation email had ever arrived. The account was simply created, and I, the actual address holder, was on the receiving end of TikTok's automated correspondence.

This is a structural problem, not an incidental one. Anyone can register a TikTok account using anyone else's email address, and the actual address holder receives the platform's notifications indefinitely.

## March 2026: contacting TikTok directly

On March 15, 2026, I submitted a "Report a potential privacy violation" through TikTok's privacy report form at https://www.tiktok.com/legal/report/privacy.

The first reply, from `feedback@tiktok.com`, was a templated message: "If you want to delete your account, log in and follow these steps." The reply assumed I owned the account. The whole problem was that I did not.

I replied, explaining that the account was not mine, that someone had created it using my email address without my consent, that I could not log in because I had never created the account, and that PIPEDA applied. The next reply asked me to verify ownership: signup date, first login location, registered device, registered phone number, linked third-party accounts.

I could not answer any of these, and that was precisely the point. I replied saying so. My inability to provide ownership details was itself evidence that I had not created the account, and a process that demanded ownership details from a non-user was structurally incompatible with non-user privacy complaints. I also stated that if the matter was not resolved within 30 days, I would file a formal complaint with the OPC.

After further escalation, `@chezou2` was eventually deleted. I did not get an explicit confirmation; I just noticed, when I checked on April 16, that the profile no longer existed.

## April 2026: the same problem, again

The same day I confirmed `@chezou2` was gone (April 16, 2026, the day after the 30-day deadline I had given TikTok), I started receiving emails from a different sender (`notification@service.tiktok.com`, with `Reply-To: edm.feedback@tiktok.com`). This time addressed to a new handle I also did not own. Messages in French, purporting to be social notifications from various TikTok users.

After `@chezou2` was deleted, someone else had created another account using my email address, and TikTok's notification machinery had picked up where it left off.

This made the issue clear. **Deleting individual accounts will not fix anything as long as TikTok does not verify email ownership at registration.** The cycle can repeat indefinitely.

A small but telling detail: the `Reply-To` address on these emails is `edm.feedback@tiktok.com`. In email marketing, "EDM" stands for "Electronic Direct Mail." TikTok's own infrastructure treats these notifications as part of its marketing email stack. This matters under CASL, as I will get to.

## Two regulatory routes in Canada

I decided that filing individual deletion requests was a losing game and turned to the regulators. There are two distinct complaints that apply.

### CASL → CRTC

CASL regulates the sending of unsolicited "commercial electronic messages" (CEMs). The relevant points for my case:

- The CRTC has the power to impose substantial monetary penalties for violations.
- TikTok's notification emails encourage engagement with the TikTok platform. They can plausibly be characterized as promoting commercial activity.
- The transactional or account-notification exemption should not apply here, because **I am not the account holder**. TikTok has not verified, and structurally cannot verify, that my email address belongs to the account being notified.

The reporting channel is the [CRTC Spam Reporting Centre](https://www.fightspam.gc.ca/) at `spam@fightspam.gc.ca`. A useful detail: you can simply email reports there, and forwarding the offending messages as `.eml` attachments preserves the full headers. This is better evidence than what the online form captures.

I sent one context email and attached five sample messages in `.eml` format.

A caveat on expectations: the SRC does not provide individual case feedback. Submissions feed an enforcement-targeting dataset; you do not get a "your case has been resolved" notice. The CASL route is about contributing to enforcement signal, not about getting a personal resolution.

### PIPEDA → OPC

PIPEDA governs the collection, use, and disclosure of personal information. The relevant provision here is Schedule 1, [**Principle 4.3 (Consent)**](https://laws-lois.justice.gc.ca/eng/acts/p-8.6/FullText.html#h-417659), read together with [**Section 6.1**](https://laws-lois.justice.gc.ca/eng/acts/p-8.6/FullText.html#h-417033) **(Valid consent)**.

Formal complaints to the OPC are filed through their [online form](https://services.priv.gc.ca/plainte-complaint-lprpde-pipeda/en/register). Two things to know in advance.

#### The form's automatic stop

The form asks whether you have filed a complaint about the same matter with another body. I had filed with the CRTC SRC eight days earlier, so I answered "Yes." The form ended my session: "If your complaint to another body covers any of your concerns with your personal information, please end this session and complete that complaint process first."

The problem: the SRC does not issue case outcomes. Waiting for that process to "complete" would mean never filing a PIPEDA complaint at all. The OPC's online form was treating CASL and PIPEDA as overlapping, when in fact they cover different conduct.

#### Recovering through the Information Centre

The OPC's [Information Centre](https://www.priv.gc.ca/en/contact-the-opc/contact-the-information-centre/) accepts free-text inquiries up to 2,000 characters. I sent one explaining the situation, the difference between the CRTC and PIPEDA matters, and asked how to proceed past the form's stop.

A reply came within a day. The OPC suggested:

- Contacting TikTok's privacy contact (TikTok Inc., Culver City) in writing first.
- Then filing a formal complaint if unresolved.
- For the form's "complaint with another body" question, **answer "No" and explain the situation in the free-text section**.

The first point was easy. I had already done the equivalent in March, through TikTok's own privacy report form (the same channel the OPC pointed me to) and the email correspondence that followed.

#### Filing the formal complaint

The OPC online form is structured in three parts. Part A asks about steps already taken. Part B determines jurisdiction. Part C covers details and remedy. Part C has four free-text fields with character limits ranging from 500 to 2,500.

The argument I built:

- **Principle 4.3 (Consent), read with s.6.1 (Valid consent).** TikTok cannot have any basis to believe the address holder consented, because it has no mechanism to verify email ownership. Section 6.1 requires that "an individual to whom the organization's activities are directed would understand the nature, purpose and consequences" of the collection, use, or disclosure. TikTok cannot satisfy this when it has not even confirmed who the address holder is.
- **No s.7 exception applies.** I am not a customer; there is no investigation, emergency, or any other listed basis.
- **Reasonable expectations of a non-user.** PIPEDA Report of Findings [#2012-002](https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2012/pipeda-2012-002/) (Facebook using non-members' email addresses to suggest friends) is directly on point. The Commissioner there found that a non-user could not reasonably expect a platform to use their email to create social connections, particularly when there is no prior relationship to the organization. The same logic applies to me and TikTok.
- **Recurrence as evidence.** A second account appearing after the first one was deleted demonstrates that the issue is systemic, not an isolated incident.

What I asked for, in order of priority:

1. A **Compliance Agreement under** [**s.17.1**](https://laws-lois.justice.gc.ca/eng/acts/p-8.6/FullText.html#h-417322) requiring TikTok to implement email verification at registration and a non-ownership-based privacy complaint process.
2. Deletion of all accounts currently associated with my email.
3. Adding my email to a registration blocklist.
4. A public Report of Findings, given the systemic nature of the issue.

Attachments (within the 8-page and 25 MB limit): the March TikTok Support thread as a PDF, the OPC Information Centre response, the November security notification, and one representative April notification message.

## Existing OPC × TikTok context

Worth knowing: in September 2025, the OPC, the CAI (Quebec), the OIPC BC, and the OIPC AB jointly issued [PIPEDA Findings #2025-003](https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2025/pipeda-2025-003/) on TikTok. That investigation focused on minors' consent and targeted advertising, not on non-user account creation, but the regulators have already concluded that TikTok's overall consent practices have problems.

That report also addressed the BC PIPA and PIPEDA jurisdictional question. In cross-border data flows, the federal and provincial laws operate in an "airtight seal" rather than excluding each other. As a BC resident filing against a Singapore-based organization, this confirms PIPEDA jurisdiction is appropriate.

So my complaint is not an isolated grievance. It joins an existing thread of regulatory scrutiny, from a different angle.

## What I did, in summary

If you found this post because you are dealing with a similar situation, here is the sequence of what I did. The disclaimer at the top of the post still applies: this is not legal advice, and your situation may differ in ways that matter.

**Step 0: Preserve evidence.**

- Save the suspicious emails: sender, date, body, and full headers.
- If they are in your spam folder, rescue them before they auto-delete (Gmail purges spam after 30 days).
- Note the unauthorized account handle(s) referenced in the messages.

**Step 1: Contact the organization in writing.**

- Use whatever privacy reporting channel the organization provides (form, email, etc.).
- Cite PIPEDA explicitly. It changes the tone of the conversation.
- Make it clear you are not the account holder and are demanding deletion as the email holder, not as the user.
- Set a reasonable deadline. Mine was 30 days. This is not a statutory requirement, just a tactical one.

**Step 2: Report to the CRTC SRC under CASL** (if the messages have any commercial or promotional flavor).

- Email `spam@fightspam.gc.ca` directly. Forward the offending messages as `.eml` attachments to preserve headers.
- Do not expect individual case feedback. The SRC uses submissions for enforcement targeting.

**Step 3: File a PIPEDA complaint with the OPC.**

- If unsure how to proceed, send an inquiry to the OPC [Information Centre](https://www.priv.gc.ca/en/contact-the-opc/contact-the-information-centre/) first (2,000-character limit; replies typically come within a day or two).
- File the [formal complaint](https://services.priv.gc.ca/plainte-complaint-lprpde-pipeda/en/register) once you have a clear path.
- Attachments are limited to roughly 8 pages and 25 MB. Choose evidence carefully. The full thread of correspondence with the organization is the most important.

**Things to be aware of.**

- The OPC has a current backlog. Investigations can take months.
- The OPC does not have order-making power. It cannot impose fines or issue binding orders directly. The strongest tool it has is the Compliance Agreement under s.17.1, which is enforceable in Federal Court. Worth asking for explicitly.
- BC OIPC may have concurrent jurisdiction, but in cross-border situations the OPC handles routing.

## A note on AI-assisted research

Parts of the research, drafting, and form responses for this complaint were done with the help of an LLM (Claude). It was useful for surfacing precedents, building arguments structurally, and drafting boilerplate quickly. It was also wrong about some specifics. For example, an early version of the analysis presented "30 days for organization response" as a PIPEDA requirement, which it is not. I caught that on a later pass, but the principle is general.

**If you do this kind of research with an AI assistant, treat its output as a starting point, not as a citation.** Verify every legal reference (statute number, section, finding number, deadline, jurisdiction) against the primary source, such as laws-lois.justice.gc.ca for legislation, priv.gc.ca for OPC findings, or fightspam.gc.ca for CASL, before acting on it. AI tools hallucinate, and acting on a hallucinated regulatory deadline is the kind of mistake that has real consequences.

For me, the value was in the working pattern. The LLM did the research scaffolding, I verified the primary sources, and I made the decisions about what went into formal submissions. That division of labour was practical and, I think, the right way to use these tools for legal-adjacent work.

***

> [!IMPORTANT]
> **Reminder:** Not legal advice. Verify primary sources. Consult a lawyer if your situation involves significant legal or financial stakes.
