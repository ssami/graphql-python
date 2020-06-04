from graphene import ObjectType, String, Schema, Int, List


class Character(ObjectType):
    first_name = String()
    last_name = String()


class Book(ObjectType):
    title = String()
    characters = List(Character)


def create_sample_books():
    book_1 = Book()
    book_1.title = 'Strong Poison'
    char_1 = Character()
    char_1.first_name = 'Peter'
    char_1.last_name = 'Wimsey'
    char_2 = Character()
    char_2.first_name = 'Bunter'
    char_2.last_name = 'Bunter'

    book_1.characters = [char_1, char_2]

    book_2  = Book()
    book_2.title = 'Gaudy Night'
    char1 = Character()
    char1.first_name = 'Peter'
    char1.last_name = 'Wimsey'
    char2 = Character()
    char2.first_name = 'Harriet'
    char2.last_name = 'Vane'
    book_2.characters = [char1, char2]

    sample_books = [book_1, book_2]
    return sample_books


class BookQuery(ObjectType):
    """
    First define the kind of query you want to make.
    We want to find the titles of book, and the characters that appear in them.
    query {
        books {
            title
            characters {
                name
            }
        }
    }
    """

    books = List(Book)
    sample_books = create_sample_books()

    @classmethod
    def resolve_books(cls, root, info):
        return cls.sample_books


book_schema = Schema(BookQuery)


if __name__ == "__main__":
    query_string = "{ books { title, characters { lastName } } } "
    result = book_schema.execute(query_string)
    print(result.data['books'])


