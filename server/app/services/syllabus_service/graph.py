from langgraph.graph import END, MessageGraph
# from langgraph.prebuilt import ToolExecutor
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.runnables import Runnable
from typing import Annotated
from operator import itemgetter

# Define the "tools" or nodes
def collect_user_info(messages: list):
    from app.services.user_onboarding.collect import handle_user_onboarding
    return handle_user_onboarding(messages)

def generate_syllabus(messages: list):
    # In a real app, you would generate the syllabus here using the collected info
    final_content = (
        "Your personalized syllabus is ready based on the information you've provided."
    )
    return {"messages": messages + [HumanMessage(content=final_content)]}

# Build the graph
builder = MessageGraph()

# Add nodes
builder.add_node("collect_user_info", collect_user_info)
builder.add_node("generate_syllabus", generate_syllabus)

# Entry point
builder.set_entry_point("collect_user_info")

# Conditional logic to pause and wait for human input before resuming
def router(messages: list):
    # If the last message is a tool message from the user, move to generation
    if any(isinstance(m, ToolMessage) and m.tool_call_id == "user_input" for m in messages):
        return "generate_syllabus"
    return "collect_user_info"

builder.add_conditional_edges("collect_user_info", router)

# Finish graph
builder.add_edge("generate_syllabus", END)

# Compile the graph
syllabus_graph = builder.compile()

# Optional helper to print the graph structure
def show_syllabus_graph():
    print("\nSyllabus Graph Structure:")
    syllabus_graph.get_graph().print_ascii()

def get_graph() -> Runnable:
    """
    Returns the syllabus graph as a runnable.
    """
    return syllabus_graph