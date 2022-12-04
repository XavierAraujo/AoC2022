from __future__ import annotations
from utils import print_answer
from dataclasses import dataclass

CHALLENGE_INPUT = "./resources/day4-input1.txt"


@dataclass
class ElfJob:
    lower_section: int
    higher_section: int

    def contains(self, other: ElfJob) -> bool:
        return self.lower_section <= other.lower_section and self.higher_section >= other.higher_section

    def overlaps(self, other: ElfJob) -> bool:
        return self.lower_section <= other.lower_section <= self.higher_section or \
               self.lower_section <= other.higher_section <= self.higher_section or \
               other.lower_section <= self.higher_section <= other.higher_section or \
               other.lower_section <= self.higher_section <= other.higher_section


def challenge1():
    count = 0
    with open(CHALLENGE_INPUT, 'r') as f:
        for line in f.read().splitlines():
            elf1_job, elf2_job = parse_elf_pair_input(line)
            if elf1_job.contains(elf2_job) or elf2_job.contains(elf1_job):
                count += 1
    return count


def challenge2():
    count = 0
    with open(CHALLENGE_INPUT, 'r') as f:
        for line in f.read().splitlines():
            elf1_job, elf2_job = parse_elf_pair_input(line)
            if elf1_job.overlaps(elf2_job):
                count += 1
    return count


def parse_elf_pair_input(elves_sections: str) -> (ElfJob, ElfJob):
    elf1_sections, elf2_sections = tuple(elves_sections.split(','))
    return ElfJob(*(int(section) for section in tuple(elf1_sections.split('-')))), \
           ElfJob(*(int(section) for section in tuple(elf2_sections.split('-'))))


if __name__ == '__main__':
    print_answer("challenge 1", challenge1)
    print_answer("challenge 2", challenge2)
