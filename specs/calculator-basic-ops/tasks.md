# Tasks: Basic Calculator CLI Program

**Input**: Design documents from `/specs/calculator-basic-ops/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Test tasks are included as they are crucial for validating the calculator's functionality.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create `src` directory
- [ ] T002 Create `src/calculator.py`
- [ ] T003 Create `main.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Setup basic `unittest` or `pytest` structure for `tests/unit/test_calculator.py`
- [ ] T005 Setup basic `unittest` or `pytest` structure for `tests/integration/test_main.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Perform Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: Implement the core arithmetic operations and basic CLI interaction for valid inputs.

**Independent Test**: Can be fully tested by running the main program, entering two numbers and a valid operator, and verifying the correct output.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T006 [P] [US1] Write unit tests for `add`, `subtract`, `multiply` in `tests/unit/test_calculator.py`
- [ ] T007 [P] [US1] Write integration test for successful addition in `tests/integration/test_main.py`
- [ ] T008 [P] [US1] Write integration test for successful subtraction in `tests/integration/test_main.py`
- [ ] T009 [P] [US1] Write integration test for successful multiplication in `tests/integration/test_main.py`

### Implementation for User Story 1

- [ ] T010 [P] [US1] Implement `add(a,b)` function in `src/calculator.py`
- [ ] T011 [P] [US1] Implement `subtract(a,b)` function in `src/calculator.py`
- [ ] T012 [P] [US1] Implement `multiply(a,b)` function in `src/calculator.py`
- [ ] T013 [US1] Add welcome message "Welcome to the Simple CLI Calculator!" to `main.py`
- [ ] T014 [US1] Add user input prompts for two numbers and an operator to `main.py`
- [ ] T015 [US1] Add operator selection logic to `main.py` to call the correct arithmetic function
- [ ] T016 [US1] Display final result in `main.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Handle Division by Zero (Priority: P1)

**Goal**: Ensure division by zero is handled gracefully with an informative error message.

**Independent Test**: Can be fully tested by running the program, entering two numbers with the second number being zero and the operator being division, and verifying the error message.

### Tests for User Story 2 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T017 [P] [US2] Write unit test for `divide` with zero-division handling in `tests/unit/test_calculator.py`
- [ ] T018 [P] [US2] Write integration test for division by zero error in `tests/integration/test_main.py`

### Implementation for User Story 2

- [ ] T019 [US2] Implement `divide(a,b)` function with zero-division handling in `src/calculator.py`
- [ ] T020 [US2] Update `main.py` to display the specific error message for division by zero.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Handle Invalid Input (Priority: P2)

**Goal**: Provide clear error messages for invalid numeric or operator inputs without crashing the program.

**Independent Test**: Can be tested by providing non-numeric input for numbers or an unsupported operator and verifying the error message.

### Tests for User Story 3 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T021 [P] [US3] Write integration test for invalid number input in `tests/integration/test_main.py`
- [ ] T022 [P] [US3] Write integration test for invalid operator input in `tests/integration/test_main.py`

### Implementation for User Story 3

- [ ] T023 [US3] Implement input validation for numbers in `main.py`
- [ ] T024 [US3] Implement input validation for operators (+, -, *, /) in `main.py`
- [ ] T025 [US3] Update `main.py` to display appropriate error messages for invalid inputs.

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T026 Code cleanup and refactoring (if necessary)
- [ ] T027 Ensure all user stories align with success criteria

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories. Builds on the `divide` function.
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Builds on the input handling in `main.py`.

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Write unit tests for add, subtract, multiply in tests/unit/test_calculator.py"
Task: "Write integration test for successful addition in tests/integration/test_main.py"
Task: "Write integration test for successful subtraction in tests/integration/test_main.py"
Task: "Write integration test for successful multiplication in tests/integration/test_main.py"

# Launch arithmetic function implementations together:
Task: "Implement add(a,b) function in src/calculator.py"
Task: "Implement subtract(a,b) function in src/calculator.py"
Task: "Implement multiply(a,b) function in src/calculator.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1
4.  **STOP and VALIDATE**: Test User Story 1 independently
5.  Deploy/demo if ready

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready
2.  Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3.  Add User Story 2 → Test independently → Deploy/Demo
4.  Add User Story 3 → Test independently → Deploy/Demo
5.  Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together
2.  Once Foundational is done:
    -   Developer A: User Story 1
    -   Developer B: User Story 2
    -   Developer C: User Story 3
3.  Stories complete and integrate independently

---

## Notes

-   [P] tasks = different files, no dependencies
-   [Story] label maps task to specific user story for traceability
-   Each user story should be independently completable and testable
-   Verify tests fail before implementing
-   Commit after each task or logical group
-   Stop at any checkpoint to validate story independently
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence