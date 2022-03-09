"""
Defining types.
Copyright (C) 2021 Vadim Vergasov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
Source of inspiration: https://github.com/eternnoir/pyTelegramBotAPI/blob/master/telebot/types.py
"""
import json


class Dictionaryable(object):
    """
    Subclasses of this class are guaranteed to be able to be converted to dictionary.
    All subclasses of this class must override to_dict.
    """

    def to_dict(self):
        """
        Returns a DICT with class field values
        This function must be overridden by subclasses.
        :return: a DICT
        """
        raise NotImplementedError


class JSONDeserializable(object):
    """
    Subclasses of this class are guaranteed to be able to be created from a json-style dict or json formatted string.
    All subclasses of this class must override de_json.
    """

    @classmethod
    def from_json(cls, json_string):
        """
        Returns an instance of this class from the given json dict or string.
        This function must be overridden by subclasses.
        :return: an instance of this class created from the given json dict or string.
        """
        raise NotImplementedError

    @staticmethod
    def check_json(json_type):
        """
        Checks whether json_type is a dict or a string. If it is already a dict, it is returned as-is.
        If it is not, it is converted to a dict by means of json.loads(json_type)
        :param json_type:
        :return:
        """
        if isinstance(json_type, dict):
            return json_type
        if isinstance(json_type, str):
            return json.loads(json_type)
        raise ValueError("json_type should be a json dict or string.")

    def __str__(self):
        d = {}
        for x, y in self.__dict__.items():
            if hasattr(y, "__dict__"):
                d[x] = y.__dict__
            else:
                d[x] = y
        return str(d)


class User(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        handle = obj["handle"]
        email = obj.get("email")
        vk_id = obj.get("vkId")
        open_id = obj.get("openId")
        first_name = obj.get("firstName")
        last_name = obj.get("lastName")
        country = obj.get("country")
        city = obj.get("city")
        organization = obj.get("organization")
        contribution = obj["contribution"]
        rank = obj.get("rank")
        rating = obj.get("rating")
        max_rank = obj.get("maxRank")
        max_rating = obj.get("maxRating")
        last_online = obj["lastOnlineTimeSeconds"]
        registration_time_seconds = obj["registrationTimeSeconds"]
        friend_of_count = obj["friendOfCount"]
        avatar = obj["avatar"]
        title_photo = obj["titlePhoto"]
        return cls(
            handle,
            email,
            contribution,
            last_online,
            registration_time_seconds,
            friend_of_count,
            avatar,
            title_photo,
            vk_id,
            open_id,
            first_name,
            last_name,
            country,
            city,
            organization,
            rank,
            rating,
            max_rank,
            max_rating,
        )

    def __init__(
        self,
        handle,
        email,
        contribution,
        last_online,
        registration_time_seconds,
        friend_of_count,
        avatar,
        title_photo,
        vk_id=None,
        open_id=None,
        first_name=None,
        last_name=None,
        country=None,
        city=None,
        organization=None,
        rank=None,
        rating=None,
        max_rank=None,
        max_rating=None,
    ):
        self.handle = handle
        self.email = email
        self.vk_id = vk_id
        self.open_id = open_id
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.city = city
        self.organization = organization
        self.contribution = contribution
        self.rank = rank
        self.rating = rating
        self.max_rank = max_rank
        self.max_rating = max_rating
        self.last_online = last_online
        self.registration_time_seconds = registration_time_seconds
        self.friend_of_count = friend_of_count
        self.avatar = avatar
        self.title_photo = title_photo

    def to_dict(self):
        return {
            "handle": self.handle,
            "email": self.email,
            "vk_id": self.vk_id,
            "open_id": self.open_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "country": self.country,
            "city": self.city,
            "organization": self.organization,
            "contribution": self.contribution,
            "rank": self.rank,
            "rating": self.rating,
            "max_rank": self.max_rank,
            "max_rating": self.max_rating,
            "last_online": self.last_online,
            "registration_time_seconds": self.registration_time_seconds,
            "friend_of_count": self.friend_of_count,
            "avatar": self.avatar,
            "title_photo": self.title_photo,
        }


class BlogEntry(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        identifier = obj["id"]
        original_locale = obj["originalLocale"]
        creation_time_seconds = obj["creationTimeSeconds"]
        author_handle = obj["authorHandle"]
        title = obj["title"]
        locale = obj["locale"]
        modification_time_seconds = obj["modificationTimeSeconds"]
        allow_view_history = obj["allowViewHistory"]
        tags = obj["tags"]
        rating = obj["rating"]
        content = obj.get("content")
        return cls(
            identifier,
            original_locale,
            creation_time_seconds,
            author_handle,
            title,
            locale,
            modification_time_seconds,
            allow_view_history,
            tags,
            rating,
            content,
        )

    def __init__(
        self,
        identifier,
        original_locale,
        creation_time_seconds,
        author_handle,
        title,
        locale,
        modification_time_seconds,
        allow_view_history,
        tags,
        rating,
        content=None,
    ):
        self.id = identifier
        self.original_locale = original_locale
        self.creation_time_seconds = creation_time_seconds
        self.author_handle = author_handle
        self.title = title
        self.locale = locale
        self.modification_time_seconds = modification_time_seconds
        self.allow_view_history = allow_view_history
        self.tags = tags
        self.rating = rating
        self.content = content

    def to_dict(self):
        return {
            "id": self.id,
            "original_locale": self.original_locale,
            "creation_time_seconds": self.creation_time_seconds,
            "author_handle": self.author_handle,
            "title": self.title,
            "locale": self.locale,
            "modification_time_seconds": self.modification_time_seconds,
            "allow_view_history": self.allow_view_history,
            "tags": self.tags,
            "rating": self.rating,
            "content": self.content,
        }


class Comment(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        identifier = obj["id"]
        creation_time_seconds = obj["creationTimeSeconds"]
        commentator_handle = obj["commentatorHandle"]
        locale = obj["locale"]
        text = obj["text"]
        rating = obj["rating"]
        parent_comment_id = obj.get("parentCommentId")
        return cls(
            identifier,
            creation_time_seconds,
            commentator_handle,
            locale,
            text,
            rating,
            parent_comment_id,
        )

    def __init__(
        self,
        identifier,
        creation_time_seconds,
        commentator_handle,
        locale,
        text,
        rating,
        parent_comment_id=None,
    ):
        self.id = identifier
        self.creation_time_seconds = creation_time_seconds
        self.commentator_handle = commentator_handle
        self.locale = locale
        self.text = text
        self.rating = rating
        self.parent_comment_id = parent_comment_id

    def to_dict(self):
        return {
            "id": self.id,
            "creation_time_seconds": self.creation_time_seconds,
            "commentator_handle": self.commentator_handle,
            "locale": self.locale,
            "text": self.text,
            "rating": self.rating,
            "parent_comment_id": self.parent_comment_id,
        }


class RecentAction(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        time_seconds = obj["timeSeconds"]
        opts = dict()
        if "blogEntry" in obj:
            opts["blog_entry"] = BlogEntry.de_json(obj["blogEntry"])
        if "comment" in obj:
            opts["comment"] = Comment.de_json(obj["comment"])
        return cls(time_seconds, opts)

    def __init__(self, time_seconds, options):
        self.time_seconds = time_seconds
        for key in options:
            setattr(self, key, options[key])

    def to_dict(self):
        dictionary = {"time_seconds": self.time_seconds}
        if "blog_entry" in self.__dict__.keys():
            dictionary["blog_entry"] = self.blog_entry.to_dict()
        if "comment" in self.__dict__.keys():
            dictionary["comment"] = self.blog_entry.to_dict()
        return dictionary


class RatingChange(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        contest_id = obj["contestId"]
        contest_name = obj["contestName"]
        handle = obj["handle"]
        rank = obj["rank"]
        rating_update_time_seconds = obj["ratingUpdateTimeSeconds"]
        old_rating = obj["oldRating"]
        new_rating = obj["newRating"]
        return cls(
            contest_id,
            contest_name,
            handle,
            rank,
            rating_update_time_seconds,
            old_rating,
            new_rating,
        )

    def __init__(
        self,
        contest_id,
        contest_name,
        handle,
        rank,
        rating_update_time_seconds,
        old_rating,
        new_rating,
    ):
        self.contest_id = contest_id
        self.contest_name = contest_name
        self.handle = handle
        self.rank = rank
        self.rating_update_time_seconds = rating_update_time_seconds
        self.old_rating = old_rating
        self.new_rating = new_rating

    def to_dict(self):
        return {
            "contest_id": self.contest_id,
            "contest_name": self.contest_name,
            "handle": self.handle,
            "rank": self.rank,
            "rating_update_time_seconds": self.rating_update_time_seconds,
            "old_rating": self.old_rating,
            "new_rating": self.new_rating,
        }


class Contest(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        identifier = obj["id"]
        name = obj["name"]
        contest_type = obj["type"]
        phase = obj["phase"]
        frozen = obj["frozen"]
        duration_seconds = obj["durationSeconds"]
        start_time_seconds = obj.get("startTimeSeconds")
        relative_time_seconds = obj.get("relativeTimeSeconds")
        prepared_by = obj.get("preparedBy")
        website_url = obj.get("websiteUrl")
        description = obj.get("description")
        difficulty = obj.get("difficulty")
        kind = obj.get("kind")
        icpc_region = obj.get("icpcRegion")
        country = obj.get("country")
        city = obj.get("city")
        season = obj.get("season")
        return cls(
            identifier,
            name,
            contest_type,
            phase,
            frozen,
            duration_seconds,
            start_time_seconds,
            relative_time_seconds,
            prepared_by,
            website_url,
            description,
            difficulty,
            kind,
            icpc_region,
            country,
            city,
            season,
        )

    def __init__(
        self,
        identifier,
        name,
        contest_type,
        phase,
        frozen,
        duration_seconds=None,
        start_time_seconds=None,
        relative_time_seconds=None,
        prepared_by=None,
        website_url=None,
        description=None,
        difficulty=None,
        kind=None,
        icpc_region=None,
        country=None,
        city=None,
        season=None,
    ):
        self.id = identifier
        self.name = name
        self.contest_type = contest_type
        self.phase = phase
        self.frozen = frozen
        self.duration_seconds = duration_seconds
        self.start_time_seconds = start_time_seconds
        self.relative_time_seconds = relative_time_seconds
        self.prepared_by = prepared_by
        self.website_url = website_url
        self.description = description
        self.difficulty = difficulty
        self.kind = kind
        self.icpc_region = icpc_region
        self.country = country
        self.city = city
        self.season = season

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "contest_type": self.contest_type,
            "phase": self.phase,
            "frozen": self.frozen,
            "duration_seconds": self.duration_seconds,
            "start_time_seconds": self.start_time_seconds,
            "relative_time_seconds": self.relative_time_seconds,
            "prepared_by": self.prepared_by,
            "website_url": self.website_url,
            "description": self.description,
            "difficulty": self.difficulty,
            "kind": self.kind,
            "icpc_region": self.icpc_region,
            "country": self.country,
            "city": self.city,
            "season": self.season,
        }


class Party(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        members = list()
        for member in obj["members"]:
            members.append(Member.de_json(member))
        participant_type = obj["participantType"]
        ghost = obj["ghost"]
        team_id = obj.get("teamId")
        contest_id = obj.get("contestId")
        room = obj.get("room")
        start_time_seconds = obj.get("startTimeSeconds")
        return cls(
            members,
            participant_type,
            ghost,
            team_id,
            contest_id,
            room,
            start_time_seconds,
        )

    def __init__(
        self,
        members,
        participant_type,
        ghost,
        team_id=None,
        contest_id=None,
        room=None,
        start_time_seconds=None,
    ):
        self.members = members
        self.participant_type = participant_type
        self.ghost = ghost
        self.team_id = team_id
        self.contest_id = contest_id
        self.room = room
        self.start_time_seconds = start_time_seconds

    def to_dict(self):
        return {
            "members": [member.to_dict() for member in self.members],
            "participant_type": self.participant_type,
            "ghost": self.ghost,
            "team_id": self.team_id,
            "contest_id": self.contest_id,
            "room": self.room,
            "start_time_seconds": self.start_time_seconds,
        }


class Member(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        handle = obj["handle"]
        return cls(handle)

    def __init__(self, handle):
        self.handle = handle

    def to_dict(self):
        return {"handle": self.handle}


class Problem(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        index = obj["index"]
        name = obj["name"]
        problem_type = obj["type"]
        contest_id = obj.get("contestId")
        problemset_name = obj.get("problemsetName")
        points = obj.get("points")
        rating = obj.get("rating")
        tags = obj.get("tags")
        return cls(
            index, name, problem_type, contest_id, problemset_name, points, rating, tags
        )

    def __init__(
        self,
        index,
        name,
        problem_type,
        contest_id=None,
        problemset_name=None,
        points=None,
        rating=None,
        tags=None,
    ):
        self.index = index
        self.name = name
        self.problem_type = problem_type
        self.contest_id = contest_id
        self.problemset_name = problemset_name
        self.points = points
        self.rating = rating
        self.tags = tags

    def to_dict(self):
        return {
            "index": self.index,
            "name": self.name,
            "problem_type": self.problem_type,
            "contest_id": self.contest_id,
            "problemset_name": self.problemset_name,
            "points": self.points,
            "rating": self.rating,
            "tags": self.tags,
        }


class ProblemStatistic(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        index = obj["index"]
        solved_count = obj["solvedCount"]
        contest_id = obj.get("contestId")
        return cls(index, solved_count, contest_id)

    def __init__(self, index, solved_count, contest_id=None):
        self.index = index
        self.solved_count = solved_count
        self.contest_id = contest_id

    def to_dict(self):
        return {
            "index": self.index,
            "solved_count": self.solved_count,
            "contest_id": self.contest_id,
        }


class Submission(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        identifier = obj["id"]
        creation_time_seconds = obj["creationTimeSeconds"]
        relative_time_seconds = obj["relativeTimeSeconds"]
        problem = Problem.de_json(obj["problem"])
        author = Party.de_json(obj["author"])
        programming_language = obj["programmingLanguage"]
        testset = obj["testset"]
        passed_test_count = obj["passedTestCount"]
        time_consumed_millis = obj["timeConsumedMillis"]
        memory_consumed_bytes = obj["memoryConsumedBytes"]
        contest_id = obj.get("contestId")
        verdict = obj.get("verdict")
        points = obj.get("points")
        return cls(
            identifier,
            creation_time_seconds,
            relative_time_seconds,
            problem,
            author,
            programming_language,
            testset,
            passed_test_count,
            time_consumed_millis,
            memory_consumed_bytes,
            contest_id,
            verdict,
            points,
        )

    def __init__(
        self,
        identifier,
        creation_time_seconds,
        relative_time_seconds,
        problem,
        author,
        programming_language,
        testset,
        passed_test_count,
        time_consumed_millis,
        memory_consumed_bytes,
        contest_id=None,
        verdict=None,
        points=None,
    ):
        self.id = identifier
        self.creation_time_seconds = creation_time_seconds
        self.relative_time_seconds = relative_time_seconds
        self.problem = problem
        self.author = author
        self.programming_language = programming_language
        self.testset = testset
        self.passed_test_count = passed_test_count
        self.time_consumed_millis = time_consumed_millis
        self.memory_consumed_bytes = memory_consumed_bytes
        self.contest_id = contest_id
        self.verdict = verdict
        self.points = points

    def to_dict(self):
        return {
            "id": self.id,
            "creation_time_seconds": self.creation_time_seconds,
            "relative_time_seconds": self.relative_time_seconds,
            "problem": self.problem.to_dict(),
            "author": self.author.to_dict(),
            "programming_language": self.programming_language,
            "testset": self.testset,
            "passed_test_count": self.passed_test_count,
            "time_consumed_millis": self.time_consumed_millis,
            "memory_consumed_bytes": self.memory_consumed_bytes,
            "contest_id": self.contest_id,
            "verdict": self.verdict,
            "points": self.points,
        }


class Hack(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        identifier = obj["id"]
        creation_time_seconds = obj["creationTimeSeconds"]
        hacker = Party.de_json(obj["hacker"])
        defender = Party.de_json(obj["defender"])
        problem = Problem.de_json(obj["problem"])
        verdict = obj.get("verdict")
        test = obj.get("test")
        judge_protocol = obj.get("judgeProtocol")
        return cls(
            identifier,
            creation_time_seconds,
            hacker,
            defender,
            problem,
            verdict,
            test,
            judge_protocol,
        )

    def __init__(
        self,
        identifier,
        creation_time_seconds,
        hacker,
        defender,
        problem,
        verdict=None,
        test=None,
        judge_protocol=None,
    ):
        self.id = identifier
        self.creation_time_seconds = creation_time_seconds
        self.hacker = hacker
        self.defender = defender
        self.problem = problem
        self.verdict = verdict
        self.test = test
        self.judge_protocol = judge_protocol

    def to_dict(self):
        return {
            "id": self.id,
            "creation_time_seconds": self.creation_time_seconds,
            "hacker": self.hacker.to_dict(),
            "defender": self.defender.to_dict(),
            "problem": self.problem.to_dict(),
            "verdict": self.verdict,
            "test": self.test,
            "judge_protocol": self.judge_protocol,
        }


class RanklistRow(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        party = Party.de_json(obj["party"])
        rank = obj["rank"]
        points = obj["points"]
        penalty = obj["penalty"]
        successful_hack_count = obj["successfulHackCount"]
        unsuccessful_hack_count = obj["unsuccessfulHackCount"]
        problem_results = list()
        for problem_result in obj["problemResults"]:
            problem_results.append(ProblemResult.de_json(problem_result))
        last_submission_time_seconds = obj.get("lastSubmissionTimeSeconds")
        return cls(
            party,
            rank,
            points,
            penalty,
            successful_hack_count,
            unsuccessful_hack_count,
            problem_results,
            last_submission_time_seconds,
        )

    def __init__(
        self,
        party,
        rank,
        points,
        penalty,
        successful_hack_count,
        unsuccessful_hack_count,
        problem_results,
        last_submission_time_seconds=None,
    ):
        self.party = party
        self.rank = rank
        self.points = points
        self.penalty = penalty
        self.successful_hack_count = successful_hack_count
        self.unsuccessful_hack_count = unsuccessful_hack_count
        self.problem_results = problem_results
        self.last_submission_time_seconds = last_submission_time_seconds

    def to_dict(self):
        return {
            "party": self.party.to_dict(),
            "rank": self.rank,
            "points": self.points,
            "penalty": self.penalty,
            "successful_hack_count": self.successful_hack_count,
            "unsuccessful_hack_count": self.unsuccessful_hack_count,
            "problem_results": [
                problem_result.to_dict() for problem_result in self.problem_results
            ],
            "last_submission_time_seconds": self.last_submission_time_seconds,
        }


class ProblemResult(JSONDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        points = obj["points"]
        rejected_attempt_count = obj["rejectedAttemptCount"]
        problem_type = obj["type"]
        best_submission_time_seconds = obj.get("bestSubmissionTimeSeconds")
        penalty = obj.get("penalty")
        return cls(
            points,
            rejected_attempt_count,
            problem_type,
            best_submission_time_seconds,
            penalty,
        )

    def __init__(
        self,
        points,
        rejected_attempt_count,
        problem_type,
        best_submission_time_seconds=None,
        penalty=None,
    ):
        self.points = points
        self.penalty = penalty
        self.rejected_attempt_count = rejected_attempt_count
        self.problem_type = problem_type
        self.best_submission_time_seconds = best_submission_time_seconds

    def to_dict(self):
        return {
            "points": self.points,
            "penalty": self.penalty,
            "rejected_attempt_count": self.rejected_attempt_count,
            "problem_type": self.problem_type,
            "best_submission_time_seconds": self.best_submission_time_seconds,
        }
