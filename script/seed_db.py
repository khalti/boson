import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.database import SessionLocal, Base, engine
from app.models.user import User
from app.models.job import Job
from app.models.candidate import Candidate
from app.core.security import get_password_hash

def seed():
    # Drop and recreate tables to apply schema changes
    print("Dropping and recreating database tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:

        # Seed Users
        print("Seeding Users...")
        backup_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users_backup.json")
        if os.path.exists(backup_path):
            import json
            print(f"Loading users from backup: {backup_path}")
            with open(backup_path, "r", encoding="utf-8") as f:
                backup_users = json.load(f)
            for user_data in backup_users:
                user = User(
                    id=user_data.get("id"),
                    name=user_data.get("name"),
                    email=user_data.get("email"),
                    hashed_password=user_data.get("hashed_password"),
                    role=user_data.get("role")
                )
                db.add(user)
        else:
            print("No users backup found. Seeding default users...")
            admin = User(
                name="Admin User",
                email="admin@khalti.com",
                hashed_password=get_password_hash("password123"),
                role="SUPERADMIN"
            )
            recruiter = User(
                name="Recruiter User",
                email="recruiter@khalti.com",
                hashed_password=get_password_hash("password123"),
                role="RECRUITER"
            )
            db.add(admin)
            db.add(recruiter)
        db.commit()

        # Seed Jobs
        print("Seeding Jobs...")
        jobs = [
            Job(
                id="data-analyst",
                title="Data Analyst",
                department="Product & Technology",
                location="Kathmandu, Nepal",
                type="Full-time",
                description=(
                    "As a Data Analyst at Khalti, you'll partner with product, growth and risk teams to translate "
                    "raw transaction data into clear, actionable insights. You'll own dashboards, deep dives and "
                    "experimentation analysis end-to-end.\n\n"
                    "Key Responsibilities:\n"
                    "- Design and maintain dashboards for product, growth and risk teams\n"
                    "- Run deep dives on user behavior, retention and transaction patterns\n"
                    "- Partner with PMs to design and analyze A/B experiments\n"
                    "- Build clean, reliable data models in our warehouse\n"
                    "- Present findings to leadership in clear, narrative form\n\n"
                    "Requirements:\n"
                    "- 2+ years of analytics experience, ideally in fintech or consumer tech\n"
                    "- Strong SQL and proficiency with Python or R\n"
                    "- Experience with BI tools (Metabase, Looker, Tableau)\n"
                    "- Comfort communicating insights to non-technical stakeholders\n"
                    "- Bachelor's degree in a quantitative field"
                ),
                skills=["Python", "SQL", "Tableau", "Metrics", "BI Tools"],
                applicants=0,
                postedDate=datetime.utcnow()
            ),
            Job(
                id="head-of-risk",
                title="Head of Risk & Compliance",
                department="Risk & Compliance",
                location="Kathmandu, Nepal",
                type="Full-time",
                description=(
                    "We're looking for a senior leader to own our end-to-end risk and compliance function — "
                    "from fraud prevention and AML to NRB regulatory engagement.\n\n"
                    "Key Responsibilities:\n"
                    "- Build and lead the risk, fraud and compliance team\n"
                    "- Own AML/KYC programs and NRB regulatory reporting\n"
                    "- Define risk appetite and policy framework across products\n"
                    "- Partner with engineering on fraud detection tooling\n"
                    "- Represent Khalti with regulators and industry bodies\n\n"
                    "Requirements:\n"
                    "- 8+ years in risk/compliance, with leadership experience\n"
                    "- Deep knowledge of Nepal's financial regulations and NRB guidelines\n"
                    "- Strong background in fraud, AML and KYC\n"
                    "- Excellent stakeholder management skills\n"
                    "- Relevant certifications (CAMS, CFE) a strong plus"
                ),
                skills=["Compliance", "Risk Management", "AML/KYC", "NRB Guidelines", "Financial Crime"],
                applicants=0,
                postedDate=datetime.utcnow()
            ),
            Job(
                id="python-django-developer",
                title="Python / Django Developer",
                department="Product & Technology",
                location="Kathmandu, Nepal (Hybrid)",
                type="Full-time",
                description=(
                    "Join our backend platform team to design, build and operate the Django services at the "
                    "heart of Khalti's payment flows.\n\n"
                    "Key Responsibilities:\n"
                    "- Design and ship Django/DRF services for payments and wallets\n"
                    "- Write well-tested, production-grade Python code\n"
                    "- Improve reliability, latency and observability across services\n"
                    "- Collaborate with product, mobile and web engineers\n"
                    "- Mentor junior engineers and contribute to code reviews\n\n"
                    "Requirements:\n"
                    "- 3+ years building production systems with Django/DRF\n"
                    "- Strong understanding of PostgreSQL and relational modeling\n"
                    "- Experience with Redis, Celery and async workflows\n"
                    "- Solid grasp of REST API design and security\n"
                    "- Comfort with Git, CI/CD and Linux environments"
                ),
                skills=["Python", "Django", "PostgreSQL", "Redis", "REST APIs", "Git"],
                applicants=0,
                postedDate=datetime.utcnow()
            ),
            Job(
                id="devops-engineer",
                title="DevOps Engineer",
                department="Product & Technology",
                location="Kathmandu, Nepal",
                type="Full-time",
                description=(
                    "You'll shape our cloud platform, CI/CD and observability stack so engineers can ship safely "
                    "many times a day.\n\n"
                    "Key Responsibilities:\n"
                    "- Operate and improve our Kubernetes-based platform\n"
                    "- Build and maintain CI/CD pipelines\n"
                    "- Drive reliability, incident response and post-mortems\n"
                    "- Strengthen security posture across infra\n"
                    "- Champion developer experience improvements\n\n"
                    "Requirements:\n"
                    "- 3+ years in DevOps/SRE roles\n"
                    "- Hands-on with Kubernetes, Docker and Terraform\n"
                    "- Experience with AWS or GCP\n"
                    "- Strong Linux and networking fundamentals\n"
                    "- Scripting in Python, Go or Bash"
                ),
                skills=["Kubernetes", "Docker", "Terraform", "AWS", "CI/CD", "Linux"],
                applicants=0,
                postedDate=datetime.utcnow()
            ),
            Job(
                id="mobile-app-developer",
                title="Mobile App Developer",
                department="Product & Technology",
                location="Kathmandu, Nepal",
                type="Full-time",
                description=(
                    "We're hiring a mobile engineer to build delightful, performant features across our "
                    "Android and iOS apps.\n\n"
                    "Key Responsibilities:\n"
                    "- Build new features in our native and cross-platform mobile apps\n"
                    "- Obsess over performance, crash-rate and UX polish\n"
                    "- Collaborate closely with design and backend teams\n"
                    "- Contribute to mobile architecture decisions\n"
                    "- Help shape our release and testing practices\n\n"
                    "Requirements:\n"
                    "- 2+ years building production mobile apps\n"
                    "- Strong skills in Kotlin/Swift or React Native/Flutter\n"
                    "- Comfortable with REST APIs and async flows\n"
                    "- Eye for detail in UI and animation\n"
                    "- Familiarity with app store release processes"
                ),
                skills=["Kotlin", "Swift", "React Native", "Flutter", "REST APIs", "Mobile UX"],
                applicants=0,
                postedDate=datetime.utcnow()
            )
        ]
        
        for job in jobs:
            db.add(job)
        db.commit()

        # Seed Candidates
        print("Seeding Candidates...")
        candidates = [
            # Strong Fit for Django role
            Candidate(
                jobId="python-django-developer",
                name="Aarav Shrestha",
                email="aarav.shrestha@example.com",
                phone="+977 9851012345",
                avatar="https://api.dicebear.com/9.x/initials/svg?seed=Aarav%20Shrestha&backgroundType=gradientLinear&fontWeight=600",
                title="Software Engineer",
                company="Leapfrog Technology",
                experience=3.0,
                location="Kathmandu, Nepal",
                education="Bachelor of Computer Engineering",
                educationHistory=[
                    {"degree": "Bachelor of Computer Engineering", "school": "Pulchowk Campus, IOE", "start": "2017-11-01", "end": "2021-08-01"}
                ],
                skills=["Python", "Django", "PostgreSQL", "Docker", "AWS", "REST APIs", "Git"],
                missingSkills=[],
                languages=[{"name": "Nepali", "level": "Native"}, {"name": "English", "level": "Professional"}],
                certifications=["AWS Certified Cloud Practitioner"],
                achievements=["Best Innovation Award at Hackfest Nepal 2022"],
                links={"linkedin": "https://linkedin.com/in/aarav-shrestha", "github": "https://github.com/aaravshrestha"},
                workHistory=[
                    {"role": "Software Engineer", "company": "Leapfrog Technology", "start": "2021-09-01", "end": "", "description": "Owned core payment service integrations."}
                ],
                salaryExpectation="NPR 180,000 / month",
                availability="30 Days",
                workAuthorization="Authorized",
                noticePeriod="30 days",
                source="Careers Page",
                stage="Interview",
                pastStages=["Applied", "Interview"],
                match=88,
                tier="Strong Fit",
                summary="A highly competent Django engineer with strong database and cloud deployment skills.",
                scores=[
                    {"criteria": "Relevant Experience", "weight": 25, "score": 23, "reason": "3+ years hands-on Django & payments backend systems."},
                    {"criteria": "Years of Relevant Experience", "weight": 20, "score": 18, "reason": "Meets 3-5 years range perfectly."},
                    {"criteria": "Education & Qualifications", "weight": 15, "score": 14, "reason": "Pulchowk Campus computer engineering graduate."},
                    {"criteria": "Trainings & Certifications", "weight": 15, "score": 10, "reason": "AWS Cloud Practitioner certified."},
                    {"criteria": "Technical Knowledge", "weight": 10, "score": 9, "reason": "Strong in python/django/postgres stack."},
                    {"criteria": "Leadership & Strategic Ability", "weight": 10, "score": 8, "reason": "Mentored interns and owned core features."},
                    {"criteria": "Communication & Soft Skills", "weight": 5, "score": 5, "reason": "Excellent team collaborator."}
                ],
                strengths=["Strong Django & DRF proficiency", "Excellent database performance skills", "AWS cloud practitioner certification"],
                weaknesses=["Limited event-driven system experience"],
                appliedDate=datetime.utcnow()
            ),
            # Moderate Fit for Data Analyst
            Candidate(
                jobId="data-analyst",
                name="Sita Thapa",
                email="sita.thapa@example.com",
                phone="+977 9801234567",
                avatar="https://api.dicebear.com/9.x/initials/svg?seed=Sita%20Thapa&backgroundType=gradientLinear&fontWeight=600",
                title="Junior Data Analyst",
                company="F1Soft International",
                experience=1.5,
                location="Lalitpur, Nepal",
                education="BSc in Computer Science",
                educationHistory=[
                    {"degree": "BSc in CSIT", "school": "St. Xavier's College", "start": "2018-09-01", "end": "2022-07-01"}
                ],
                skills=["SQL", "Python", "Tableau", "Excel"],
                missingSkills=["Metrics", "BI Tools"],
                languages=[{"name": "Nepali", "level": "Native"}, {"name": "English", "level": "Fluent"}],
                certifications=[],
                achievements=[],
                links={"linkedin": "https://linkedin.com/in/sita-thapa"},
                workHistory=[
                    {"role": "Junior Analyst", "company": "F1Soft International", "start": "2022-09-01", "end": "", "description": "Designed dashboards using Tableau."}
                ],
                salaryExpectation="NPR 70,000 / month",
                availability="Immediate",
                workAuthorization="Authorized",
                noticePeriod="Immediate",
                source="Careers Page",
                stage="Applied",
                pastStages=["Applied"],
                match=68,
                tier="Moderate Fit",
                summary="Promising junior data analyst with solid foundation in SQL, Python and dashboard design.",
                scores=[
                    {"criteria": "Relevant Experience", "weight": 25, "score": 18, "reason": "Good Tableau and dashboarding experience."},
                    {"criteria": "Years of Relevant Experience", "weight": 20, "score": 14, "reason": "Has 1.5 years experience, slightly below the 2+ years requirement."},
                    {"criteria": "Education & Qualifications", "weight": 15, "score": 13, "reason": "CSIT degree from St. Xavier's college."},
                    {"criteria": "Trainings & Certifications", "weight": 15, "score": 5, "reason": "No specialized certifications listed."},
                    {"criteria": "Technical Knowledge", "weight": 10, "score": 8, "reason": "Good SQL and Python foundations."},
                    {"criteria": "Leadership & Strategic Ability", "weight": 10, "score": 5, "reason": "Early-career developer with minor leadership exposure."},
                    {"criteria": "Communication & Soft Skills", "weight": 5, "score": 5, "reason": "Excellent communication skills."}
                ],
                strengths=["Solid SQL skills", "Experience with Tableau", "CSIT degree"],
                weaknesses=["Slightly under the required years of experience"],
                appliedDate=datetime.utcnow()
            ),
            # Weak Fit for Head of Risk
            Candidate(
                jobId="head-of-risk",
                name="Ramesh Adhikari",
                email="ramesh.adhikari@example.com",
                phone="+977 9841234568",
                avatar="https://api.dicebear.com/9.x/initials/svg?seed=Ramesh%20Adhikari&backgroundType=gradientLinear&fontWeight=600",
                title="Compliance Associate",
                company="Nabil Bank",
                experience=2.0,
                location="Kathmandu, Nepal",
                education="Bachelor of Business Administration",
                educationHistory=[
                    {"degree": "BBA", "school": "Ace Institute of Management", "start": "2016-09-01", "end": "2020-07-01"}
                ],
                skills=["KYC Verification", "Customer Relations"],
                missingSkills=["Compliance", "Risk Management", "AML/KYC", "NRB Guidelines", "Financial Crime"],
                languages=[{"name": "Nepali", "level": "Native"}, {"name": "English", "level": "Fluent"}],
                certifications=[],
                achievements=[],
                links={},
                workHistory=[
                    {"role": "Compliance Officer", "company": "Nabil Bank", "start": "2021-02-01", "end": "", "description": "Handled simple customer KYC verification."}
                ],
                salaryExpectation="NPR 60,000 / month",
                availability="15 Days",
                workAuthorization="Authorized",
                noticePeriod="15 days",
                source="Careers Page",
                stage="Applied",
                pastStages=["Applied"],
                match=35,
                tier="Weak Fit",
                summary="Candidate lacks required leadership and regulatory experience for Head of Risk.",
                scores=[
                    {"criteria": "Relevant Experience", "weight": 25, "score": 8, "reason": "Only basic KYC checking experience; lacks strategic risk management."},
                    {"criteria": "Years of Relevant Experience", "weight": 20, "score": 5, "reason": "2 years vs 8+ years required."},
                    {"criteria": "Education & Qualifications", "weight": 15, "score": 10, "reason": "BBA degree, non-specialized."},
                    {"criteria": "Trainings & Certifications", "weight": 15, "score": 0, "reason": "Lacks CAMS or CFE."},
                    {"criteria": "Technical Knowledge", "weight": 10, "score": 5, "reason": "Familiar with bank KYC processes."},
                    {"criteria": "Leadership & Strategic Ability", "weight": 10, "score": 3, "reason": "Lacks team leadership experience."},
                    {"criteria": "Communication & Soft Skills", "weight": 5, "score": 4, "reason": "Good team player."}
                ],
                strengths=["Basic understanding of bank KYC"],
                weaknesses=["Lacks required 8+ years experience", "No CAMS/CFE certification", "No team leadership experience"],
                appliedDate=datetime.utcnow()
            )
        ]
        
        for cand in candidates:
            db.add(cand)
            
        # Update job applicant counts in python
        for job in jobs:
            job_candidates = [c for c in candidates if c.jobId == job.id]
            job.applicants = len(job_candidates)
            
        # Seed Activity Logs
        print("Seeding Activity Logs...")
        from app.models.activity_log import ActivityLog
        from datetime import timedelta
        
        now = datetime.utcnow()
        activity_logs = [
            ActivityLog(
                timestamp=now - timedelta(days=2),
                action_type="job_created",
                description="Admin User (SUPERADMIN) created a new job: Frontend Engineer (Engineering)",
                user_name="Admin User",
                user_email="admin@khalti.com",
                job_id="frontend-engineer"
            ),
            ActivityLog(
                timestamp=now - timedelta(days=1, hours=4),
                action_type="candidate_applied",
                description="Candidate Sandesh Adhikari applied for job 'Frontend Engineer'",
                user_name="System (Applicant)",
                user_email="sandesh@gmail.com",
                job_id="frontend-engineer"
            ),
            ActivityLog(
                timestamp=now - timedelta(hours=8),
                action_type="candidate_stage_updated",
                description="Recruiter User (RECRUITER) moved candidate Sandesh Adhikari from Applied to Screening",
                user_name="Recruiter User",
                user_email="recruiter@khalti.com",
                job_id="frontend-engineer"
            ),
            ActivityLog(
                timestamp=now - timedelta(hours=2),
                action_type="job_status_updated",
                description="Admin User (SUPERADMIN) updated job 'Compliance Manager' status to Closed",
                user_name="Admin User",
                user_email="admin@khalti.com",
                job_id="compliance-manager"
            ),
        ]
        
        for log in activity_logs:
            db.add(log)
            
        db.commit()
        print("Database successfully seeded!")
        
    except Exception as e:
        db.rollback()
        print(f"Error during seeding: {e}")
        raise e
    finally:
        db.close()

if __name__ == "__main__":
    seed()
