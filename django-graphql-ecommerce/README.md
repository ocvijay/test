# Django ecommerce

A classic test app build to test graphql in Django.

# How to run?

- Run migration with `python manage.py makemigrations`
- Execute to run server using `python manage.py runserver`

## Graphql queries

Go to root url i.e. `127.0.0.1:8000/graphql`

### Example queries

### List

```
{
  categories {
    id
    title
  }
}
```

### Create

```
mutation {
  create_category: createCategory(title: "Test category") {
    category {
      id
      title
    }
  }
}
```

### Update

```
mutation {
  update_category: updateCategory(id:3, title: "Test category updated") {
    category {
      id
      title
    }
  }
}
```

### Delete

```
mutation {
  delete_category: deleteCategory(id: 3) {
    category {
      id
    }
  }
}
```