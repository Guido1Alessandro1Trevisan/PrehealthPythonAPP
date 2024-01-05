import random

easy_questions = [
    "Describe a situation where you had to work in a team to achieve a common goal.",
    "Discuss a time when you faced a moral dilemma and how you resolved it.",
    "Explain how you would handle a situation where you had to give constructive criticism to a colleague.",
    "Describe a challenge you encountered and how it changed your perspective.",
    "Discuss an experience where you had to adapt to a new environment or culture.",
    "Explain a situation where you demonstrated effective communication skills.",
    "Describe a time when you had to prioritize multiple tasks under a tight deadline.",
    "Discuss your approach to resolving conflicts in a group setting.",
    "Explain how you would handle a situation where you disagreed with a superior's decision.",
    "Describe an instance where you demonstrated empathy towards someone in need."
]

medium_questions = [
    "Discuss a situation where you faced a major ethical dilemma and the steps you took to resolve it.",
    "Explain a time when you had to make a difficult decision with limited information. How did you approach it?",
    "Describe an instance where you had to navigate a complex interpersonal conflict and the strategies you employed.",
    "Discuss a significant failure or setback in your life. What did you learn from it, and how did it shape your future actions?",
    "Explain a situation where you had to advocate for a cause or idea you were passionate about. How did you go about it?",
    "Describe an experience where you encountered a cultural or societal bias. How did you respond, and what did you learn?",
    "Discuss a project or initiative you led. What were the challenges, and how did you ensure its success?",
    "Explain how you would address a situation involving an ethical violation within your workplace or academic institution.",
    "Describe an instance where you had to balance personal values with organizational or societal expectations. How did you reconcile the differences?",
    "Discuss a time when you had to make a decision that went against popular opinion. How did you handle potential backlash?"
]

hard_questions = [
    "Discuss a complex moral dilemma in healthcare and the ethical principles involved in your decision-making process.",
    "Explain how you would approach a situation where you had to make a life-altering decision for a family member who couldn't make the decision themselves.",
    "Describe a time when you had to advocate for a marginalized group in the face of significant opposition. How did you navigate the challenges?",
    "Discuss a situation where you encountered systemic discrimination or injustice. What actions did you take to address it?",
    "Explain a time when you faced a crisis or emergency situation and had to make rapid, high-stakes decisions. What were the outcomes?",
    "Describe a project or initiative you led that required navigating complex legal and ethical considerations. How did you ensure compliance and uphold moral standards?",
    "Discuss a difficult ethical dilemma you encountered in a professional setting and how you influenced the organization's response.",
    "Explain a situation where you had to balance the interests of multiple stakeholders with conflicting agendas. How did you find a resolution?",
    "Discuss a scenario where you had to make a decision that challenged your personal beliefs and values. How did you reconcile the conflict?",
    "Describe a time when you took a principled stand on a controversial issue, even when it had personal or professional consequences. How did you handle the aftermath?"
]


def get_question():
    return random.choice(hard_questions)

