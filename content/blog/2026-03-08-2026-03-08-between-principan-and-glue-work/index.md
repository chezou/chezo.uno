---
title: Between Principal and Glue Work
date: 2026-03-08 13:07:00+00:00
draft: false
featured: true
image: {preview_only: false}
tags: [Staff Engineer]
recommendations: [/blog/2025-05-02-ml-project-and-scrum/, /blog/2020-03-05_py-operator-development-guide-for-python-users/,
  /blog/2019-11-26_how-to-release-python-package-from-github-actions-d5a1d8edba6e/]
---

## Introduction

I have always worked with the mindset that being a Staff+ Engineer is essentially doing high-level "[glue work](https://www.noidea.dog/glue)." Because the tasks are surprisingly diverse, I have written about them [in the form of book reviews](https://chezo.uno/post/2025-11-25-staff-engineering-path/), but I have never quite been able to cohesively organize my thoughts.

And for a while, I also struggled with how to effectively express the impact I've made on my resume. This is because the role requires catching things that fall through the cracks far more often than one might expect, and while delivering value through these tasks is incredibly important, resumes tend to demand flashy, shiny achievements (like [Promoware](https://www.reddit.com/r/cscareerquestions/comments/11h29cr/comment/jasjsop/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)).

My stance has always been, "I will do whatever it takes to deliver a valuable product to the customer." The scope of "whatever it takes" probably varies from person to person. So, as a starting point, let's unravel this by comparing it with Will Larson's [Staff Archetypes](https://staffeng.com/guides/staff-archetypes/), which are well-known to those familiar with [Staff Engineers](https://www.amazon.ca/Staff-Engineer-Leadership-beyond-management/dp/1736417916).

## The 4 Staff Archetypes

Let's recap Will Larson's four Staff Archetypes.

### 1\. Tech Lead

A role deeply involved with a specific team (or a few teams), leading technical direction and execution.

*   Characteristics: Takes responsibility for the team's technical decisions, fleshing out complex tasks, and unblocking progress.
    
*   Primary Activities: Focuses more on shaping the overall technical vision for the team, mentoring members, and coordinating with product managers rather than pure implementation. This is the most common archetype and a natural extension from a senior engineer role.
    

### 2\. Architect

A role responsible for cross-organizational success and quality within a specific technical domain (e.g., API design, frontend, infrastructure strategy).

*   Characteristics: Formulates technical strategies spanning multiple teams and maintains long-term technical alignment.
    
*   Primary Activities: Deeply understands business needs and technical constraints to guide the overall architecture of the organization. Needed in large organizations or companies with complex systems burdened by accumulated debt.
    

### 3\. Solver

A "firefighter" role that moves beyond a specific team to solve critical and difficult technical challenges for the organization.

*   Characteristics: Deployed to problems with high execution risk or complex issues where the solution is unclear.
    
*   Primary Activities: Goes to the frontline where the problem is occurring based on requests from leadership, and moves on to the next challenge once resolved. Requires pure technical breakthrough ability rather than organizational coordination.
    

### 4\. Right Hand

A role acting as the "right hand" to executives like the CTO or VP, borrowing their authority to solve complex organizational problems.

*   Characteristics: Operates at the intersection of technology, business, people, and processes to permeate the executive's intent throughout the organization.
    
*   Primary Activities: Attends executive meetings and helps remove organizational bottlenecks and execute strategies. A rare archetype found in massive organizations with hundreds of engineers.
    

However, Will Larson also states the following (quoted from [Staff Archetypes](https://staffeng.com/guides/staff-archetypes/)):

“This taxonomy is more focused on being _useful_ than complete, but so far, I’ve been able to fit every Staff-plus engineer I’ve spoken to into one of these categories. Admittedly, some folks are easier to classify than others.”

I started writing this article because I couldn't help but feel that I might be one of those "harder to classify" ones.

## Breaking Down My Work by Archetypes

Let me briefly explain my positioning as a Principal Software Engineer or Tech Lead at my current workplace.

I didn't have the official title of Tech Lead, but I operated as the engineer overall responsible for driving the engineering of the company's ML product development. Regarding the organizational structure, it was reorganized about a year ago by the CTO and VPoE. I, as a Principal, and the Engineering Manager of the ML team existed as peers, reporting directly to the Sr Engineering Director who oversaw multiple engineering teams. This is what is often called a "Two-in-a-box" style.

Let's break down the main things I've done over the past three years using the archetypes.

*   **As a Tech Lead / Architect**
    
    *   Consistently led the grand design, PoC, scale validation, and release of the ML training and prediction infrastructure (Python, FastAPI, AWS Batch), successfully releasing it with 2 people in 5 months.
        
    *   Scaled the RFM prediction processing, making it up to 100x faster and supporting processing for 1 billion users.
        
    *   Implemented the PoC for the recommendation ML solution model and selected scalable algorithms.
        
*   **As a Right Hand**
    
    *   Directly explained the engineering roadmap to the CTO and product leadership to secure sponsorship.
        
    *   Secured sponsorship for a complete revamp of the ML infrastructure over a year and drove it through to release.
        
    *   Drafted the product roadmap and proposed product direction not only to Engineering but also to the Product Manager and VPoP.
        
*   **As a Solver**
    
    *   When an escalation came from the PS team saying, "The customer needs this feature right now," I jumped in as a firefighter, resolved the issue, and released it to production in 1-2 weeks.
        
    *   Rewrote incomplete code from a project where the engineers originally worked on it, elevating it to production-grade.
        

As I was writing this, I realized I also paid attention to things like the following:

*   Task assignment considering members' motivation and project planning with their careers in mind (e.g., taking on tedious tasks like building admin consoles myself and handing challenging tasks to members).
    
*   Creating draft UI design proposals to communicate the complexity of the data model to UX designers.
    
*   Fundamentally rewriting JDs and acting as a gatekeeper in interviews.
    
*   Providing indirect performance evaluation input to the EM during 1:1s.
    

In short, what I was doing was essentially [glue work](https://www.noidea.dog/glue) \[^1\]. However, my focus was on catching things that fall through the cracks to prevent the project from failing and ensure its success, giving it my all according to their importance. Because of this, I often wondered what my actual responsibilities were, but reading Staff Engineer books out there made me realize that more or less everyone does this, so I gritted my teeth and kept unblocking things.

\[^1\] In the Japanese engineering community, there's a term "高機能雑用" (kōkinō zatsuyō) — roughly "High-functioning general-purpose grunt work." It originated from [an engineer](https://x.com/tokoroten/status/193359209864241152) who, when asked by his director what he actually does, replied: "I do Hadoop, Hive, MySQL, machine learning, log analysis, NLP, VBA, and firefighting — but that's too much to explain, so I just say 'High-functioning general-purpose grunt work.'" That's pretty much what being a Staff+ engineer feels like.

## Why Does the Scope of Staff+ Expand?

Generally, the Two-in-a-box model is well known, although the breadth of role division varies. For example, in "[Engineering Management: The Pendulum Or The Ladder](https://charity.wtf/2019/01/04/engineering-management-the-pendulum-or-the-ladder/)," Charity Majors writes about the collaboration between EMs and TLs:

> "There is an enormous demand for technical engineering leaders — far more demand than supply.  The most common hackaround is to pair a people manager (who can speak the language and knows the concepts, but stopped engineering ages ago) with a tech lead, and make them collaborate to co-lead the team.  This unwieldy setup often works pretty well."

Also, at [Asana](https://asana.com/inside-asana/grow-your-leadership-impact-as-a-tech-lead-or-engineering-manager), every team has an EM, and for many projects, a TL is placed separately to collaborate with the EM, or if there is no TL, a Tech Lead Manager holds both roles. In their case, the division of roles between EM and TL is as follows:

> *   Engineering Manager primarily focuses on people management (staffing, coaching & growth) and organizational strategy (organizational risk, operational efficiency, team charter & outcomes)
>     
> *   Tech Lead primarily focuses on technical leadership (technical execution, technical strategy, technical culture, roadmap feasibility & execution).
>     

In this way, the advantage of Two-in-a-box is sharing the cognitive load so that attention can be paid to various areas.

However, in domains requiring deep technical knowledge like ML, if there is a gap in the technical depth between the EM and the TL, it inevitably becomes difficult to make highly accurate technical decisions. As a result, the "division" turns into a broad "delegation" to the TL, and the scope of the TL expands. In my case, for instance, I was making decisions as a TL up to task assignment and resource allocation, being delegated some of the EM roles at Asana.

In my case, I felt the Two-in-a-box system worked better than expected. Especially after we clearly defined our boundaries and respective territories, we just ran autonomously. By fundamentally dividing roles—People Management for the EM and Technical Leadership for the TL—and reporting as peers to a common Sr Engineering Director, the expansion of the TL's scope became organizationally acceptable. Before this structure was put in place, we frequently had minor clashes that looked like we were stepping on each other's toes, which made me realize how important it is to build a good organizational structure.

Ultimately, if the EM and TL trust each other and have a system where they can work autonomously, it's a trivial matter which way the border leans a bit.

## Reflecting on My Career, or Redefining "Glue Work"

I've written a lot so far, but if I were to reorganize the work I've done and the scope I've expanded based on the Archetypes:

*   Technical decision-making and delivery as a Tech Lead/Architect
    
*   Proposing technical strategies to executives and gaining approval as a Right Hand
    
*   Critical problem-solving skills as a Solver
    
    *   Occasionally stepping into scopes beyond Staff+ (PdM, PjM, UX Designer, parts of EM) when necessary

It turns out that doing glue work as a Staff+ is not just doing random chores, but rather "carrying multiple Staff+ functions necessary for the organization all by oneself."

Will Larson might be a little surprised too.

But well, I think someone who can move like this would be highly valued in a company with a strong startup culture.

## To Those With the Same Struggles

If you ever feel like you're losing sight of your core value while doing glue work as a Staff+ engineer, I recommend looking back at the Archetypes and verbalizing what you are actually achieving.

In the AI era, verbalizing allows for deeper exploration, so it might be good to bounce ideas off an AI to articulate your thoughts. I myself have been trying this after a former colleague of mine, [Sho](https://www.linkedin.com/in/shoshimauchi/), told me that dialoguing with AI for introspection deepens self-understanding and helps find directions for growth. It demands real concentration and can be draining, but the rewards are significant.

Also, to keep me sane, the case studies in books about Staff Engineers have been a great support. It would be good to keep both [Will Larson's book](https://www.amazon.ca/Staff-Engineer-Leadership-beyond-management/dp/1736417916) and [Tanya Reilly's book](https://www.amazon.ca/Staff-Engineers-Path-Individual-Contributors/dp/1098118731) close at hand. Reading them after a painful experience provides a deeply enriching reading experience that resonates more the more you digest it.

Doing glue work might just be a sign that you are thriving as a Staff+. However, never forget to prioritize your tasks by considering their business impact.