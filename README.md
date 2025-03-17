# Unisource


INSERT INTO courses (
    crn,
    course,
    course_title,
    status,
    enrollment_capacity,
    enrollment,
    waitlist_capacity,
    waitlist_enrollment,
    projected_enrl,
    meeting_desc,
    days,
    time,
    bldgroom,
    class_room_attributes,
    rec_mtg_desc,
    recitation_days,
    recitation_time,
    recitation_bldgroom,
    rec_room_attributes,
    lab_mtg_desc,
    lab_days,
    lab_time,
    lab_bldgroom,
    lab_room_attributes,
    credit_hours,
    bill_hours,
    primary_instructor,
    primary_instructor_lin,
    secondary_instructors,
    attributes,
    part_of_term,
    schedule_code,
    special_approval,
    cross_list_code,
    link_identifier,
    link_connector,
    tuition_fees,
    campus_code,
    instructional_method,
    grade_mode,
    long_title,
    modalities,
    long_text,
    short_text
) VALUES (
    147254,                                      -- CRN
    'CSB 10000-010',                              -- Course
    'Sang Blockchain Concepts and Apps.',            -- Course Title
    'A',                                        -- Status
    40,                                         -- Enrollment Capacity
    0,                                          -- Enrollment
    0,                                          -- Waitlist Capacity
    0,                                          -- Waitlist Enrollment
    40,                                         -- Projected Enrl
    'Class On-Campus Only',                     -- Meeting Desc
    'MW',                                       -- Days
    '1335-1450',                                -- Time
    NULL,                                       -- BldgRoom (empty)
    'HyFlex 2 Classroom',                       -- Class Room Attributes
    NULL,                                       -- Rec Mtg desc (empty)
    NULL,                                       -- Recitation Days (empty)
    NULL,                                       -- Recitation Time (empty)
    NULL,                                       -- Recitation Bldgroom (empty)
    NULL,                                       -- Rec Room Attributes (empty)
    NULL,                                       -- Lab Mtg Desc (empty)
    NULL,                                       -- Lab Days (empty)
    NULL,                                       -- Lab Time (empty)
    NULL,                                       -- Lab Bldgroom (empty)
    NULL,                                       -- Lab Room Attributes (empty)
    3,                                          -- Credit Hours
    3,                                          -- Bill Hours
    'Korth, Hank',                              -- Primary Instructor
    '867091929',                                -- Primary Instructor LIN
    NULL,                                       -- Secondary Instructors (empty)
    'CAMP',                                     -- Attributes
    'Full Term',                                -- Part of Term
    'L',                                        -- Schedule Code
    NULL,                                       -- Special Approval (empty)
    NULL,                                       -- Cross List Code
    '2F',                                       -- Link Identifier
    'F2',                                       -- Link Connector (empty)
    NULL,                                       -- Tuition Fees
    'T',                                        -- Campus Code (empty)
    NULL,                                       -- Instructional Method
    NULL,                                        -- Grade Mode
    'Blockchain Concepts and Applications',     -- Long_Title (empty)
    'On-Campus Required',                       -- Modalities (empty)
    NULL,                                       -- Long Text (empty)
    NULL                                      -- Short Text (empty)                                     
);

